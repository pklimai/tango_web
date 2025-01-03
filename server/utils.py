from time import mktime
from datetime import datetime
from typing import Union, List, Iterable, Tuple, Dict

from dateutil.parser import parse as tparse
from sqlalchemy import and_, text
from sqlalchemy.engine import Engine

from server import cache, db, app
from server.config import CACHE_TIMEOUT_SEC
from server.orm.bmn import Run
from server.orm.hdbpp import AttConfDataType, AttConf
from server.typings import DomainEntry

# def utc2local(utc):
#     epoch = mktime(utc.timetuple())
#     offset = datetime.fromtimestamp(epoch) - datetime.utcfromtimestamp(epoch)
#     return utc + offset

# e.g. tparse("2021-03-19T20:18:00.000Z") = datetime.datetime(2021, 3, 19, 20, 18, tzinfo=tzutc()) = tp
# tp.timestamp() = 1616185080.0
# datetime.datetime.fromtimestamp(1616185080.0) = datetime.datetime(2021, 3, 19, 23, 18)
def prepare_datetime(time_str: str, offset_min: int) -> datetime:
    # if time_str.endswith("Z"): return utc2local(tparse(time_str))
    # return tparse(time_str)
    if time_str.endswith("Z"):
        return datetime.utcfromtimestamp(tparse(time_str).timestamp() - offset_min*60)
    return tparse(time_str)


def shorten_dt(dt):
    res = str(dt)
    if res.endswith("+00:00"):
        res = res[0:-6]
    return res


@cache.memoize(timeout=CACHE_TIMEOUT_SEC)
def _get_available_runs():
    with app.server.app_context():
        available_runs = {}
        for run in db.session.query(Run):
            if run.run_period.period_number not in available_runs:
                available_runs[run.run_period.period_number] = []
            available_runs[run.run_period.period_number].append(run.run_number)
        return [dict(period=r, numbers=available_runs[r]) for r in sorted(available_runs.keys(), reverse=True)]


@cache.memoize(timeout=CACHE_TIMEOUT_SEC)
def _get_available_attrs():
    with app.server.app_context():
        domains: List[str] = [d[0] for d in db.session.query(AttConf.domain)
                              .distinct()]

        result = {d: {} for d in domains}

        for domain in domains:
            families = [f[0] for f in db.session.query(AttConf.family)
                        .filter(AttConf.domain == domain)
                        .distinct()]
            result[domain] = {f: {} for f in families}

            for family in families:
                members = [f[0] for f in db.session.query(AttConf.member)
                           .filter(AttConf.domain == domain)
                           .filter(AttConf.family == family)
                           .distinct()]
                result[domain][family] = {m: {} for m in members}
                for member in members:
                    names = members = [n[0] for n in db.session.query(AttConf.name)
                                       .filter(AttConf.domain == domain)
                                       .filter(AttConf.family == family)
                                       .filter(AttConf.member == member)
                                       .distinct()]
                    result[domain][family][member] = names
        return result


@cache.memoize(timeout=CACHE_TIMEOUT_SEC)
def _get_run(period: int = None, run: int = None) -> Union[Run, None]:
    if period is None or run is None:
        return None
    else:
        return db.session.query(Run) \
            .filter(and_(Run.period_number == period, Run.run_number == run)).first()


@cache.memoize(timeout=CACHE_TIMEOUT_SEC)
def _get_attrs_for_params(domain: str, family: str, member: str, name: str) -> List[Tuple[int, int]]:
    with app.server.app_context():
        engine: Engine = db.get_engine('hdbpp')
        connection = engine.connect()
        return list(connection.execute(text("""
                        SELECT DISTINCT att_conf_data_type_id, att_conf_id
                        FROM att_conf
                        WHERE domain = "{}" AND family = "{}" AND member = "{}" AND name = "{}";
                    """.format(domain, family, member, name))).fetchall())


def get_values(
        att_conf_data_type_id: int, att_conf_id:
        int, start: datetime, end: datetime) -> Dict[int, List[Tuple[datetime, int]]]:
    with app.server.app_context():
        engine: Engine = db.get_engine('hdbpp')
        connection = engine.connect()
        data_type: AttConfDataType = db.session.query(
                AttConfDataType).filter(AttConfDataType.att_conf_data_type_id == att_conf_data_type_id).first()
        table_name = 'att_' + data_type.data_type

        if 'scalar' in data_type.data_type:
            sql = """
                SELECT data_time, value_r
                FROM {}
                WHERE (data_time BETWEEN "{}" AND "{}") AND att_conf_id = {};
            """.format(
                table_name,
                shorten_dt(start),
                shorten_dt(end), att_conf_id)
            # print(sql)
            return {0: connection.execute(text(sql)).fetchall()}
        elif 'array' in data_type.data_type:
            sql = """
                        SELECT idx, data_time, value_r
                        FROM {}
                        WHERE (data_time BETWEEN "{}" AND "{}") AND att_conf_id = {};
                    """.format(
                table_name,
                shorten_dt(start),
                shorten_dt(end), att_conf_id)
            # print(sql)

            data = connection.execute(text(sql)).fetchall()

            data_dict = {}
            for entry in data:
                if entry[0] not in data_dict:
                    data_dict[entry[0]] = []
                data_dict[entry[0]] += [(entry[1], entry[2]),]

            return data_dict


# @cache.memoize(timeout=CACHE_TIMEOUT_SEC)
# def _get_attrs_for_type(data_type: str):
#     types = db.session.query(
#         AttConfDataType.att_conf_data_type_id).filter(AttConfDataType.data_type == data_type)
#     att_conf_ids = db.session.query(
#         AttConf.att_conf_id).filter(AttConf.att_conf_data_type_id.in_(types))
#     return [att_conf_id[0] for att_conf_id in att_conf_ids]


# @cache.memoize(timeout=CACHE_TIMEOUT_SEC)
# def _get_attrs(start: datetime, end: datetime) -> List[int]:
#     query: Iterable[AttConfDataType] = db.session.query(AttConfDataType)
#     engine: Engine = db.get_engine(app.server, 'hdbpp')
#
#     def get_values(query_: Iterable[AttConfDataType],
#                    start_dt: datetime, end_dt: datetime) -> Iterable[int]:
#         for data_type in query_:
#
#             att_conf_ids = _get_attrs_for_type(data_type.data_type)
#
#             if not att_conf_ids:
#                 continue
#
#             table_name = 'att_' + data_type.data_type
#             sql = """
#                 SELECT DISTINCT att_conf_id
#                 FROM {}
#                 WHERE (data_time BETWEEN "{}" AND "{}") AND (att_conf_id IN ({}));
#                 """.format(
#                 table_name,
#                 shorten_dt(start_dt),
#                 shorten_dt(end_dt), ", ".join((str(i) for i in att_conf_ids)))
#
#             values: List[int] = [v[0] for v in engine.execute(sql).fetchall()]
#
#             for value in values:
#                 yield int(value)
#
#     return list(get_values(query, start, end))


# @cache.memoize(timeout=CACHE_TIMEOUT_SEC)
# def _get_run_attrs(period: int, run: int) -> List[int]:
#     run_model = _get_run(period, run)
#     return _get_attrs(run_model.start_datetime, run_model.end_datetime)


# @cache.memoize(timeout=CACHE_TIMEOUT_SEC)
# def initialize_domains(start: datetime, end: datetime) -> List[DomainEntry]:
#     """Get all available domains from database.
#     (seems to be unused)
#     """
#     attrs = _get_attrs(start, end)
#     query = db.session.query(AttConf.domain) \
#         .filter(text("att_conf_id in ({})".format(", ".join(str(v) for v in attrs)))).distinct()
#     return [
#         {'label': v[0], 'value': v[0]}
#         for v in query]
