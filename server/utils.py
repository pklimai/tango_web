from datetime import datetime
from typing import Union, List, Iterable, Tuple, Dict

from sqlalchemy import and_, text
from sqlalchemy.engine import Engine

from server import cache, db, app
from server.config import CACHE_TIMEOUT_SEC
from server.orm.bmn import Run
from server.orm.hdbpp import AttConfDataType, AttConf
from server.typings import DomainEntry


@cache.memoize(timeout=CACHE_TIMEOUT_SEC)
def _get_run(period: int = None, run: int = None) -> Union[Run, None]:
    if period is None or run is None:
        return None
    else:
        return db.session.query(Run) \
            .filter(and_(Run.period_number == period, Run.run_number == run)).first()


@cache.memoize(timeout=CACHE_TIMEOUT_SEC)
def _get_attrs_for_type(data_type: str):
    types = db.session.query(
        AttConfDataType.att_conf_data_type_id).filter(AttConfDataType.data_type == data_type)
    att_conf_ids = db.session.query(
        AttConf.att_conf_id).filter(AttConf.att_conf_data_type_id.in_(types))
    return [att_conf_id[0] for att_conf_id in att_conf_ids]


@cache.memoize(timeout=CACHE_TIMEOUT_SEC)
def _get_run_attrs(period: int, run: int) -> List[int]:
    run_model = _get_run(period, run)
    query: Iterable[AttConfDataType] = db.session.query(AttConfDataType)
    engine: Engine = db.get_engine(app.server, 'hdbpp')

    def get_values(query_: Iterable[AttConfDataType], run_: Run) -> Iterable[int]:
        for data_type in query_:

            att_conf_ids = _get_attrs_for_type(data_type.data_type)

            if not att_conf_ids:
                continue

            table_name = 'att_' + data_type.data_type
            sql = """
            SELECT DISTINCT att_conf_id
            FROM {}
            WHERE (data_time BETWEEN "{}" AND "{}") AND (att_conf_id IN ({}));
            """.format(
                table_name,
                run_.start_datetime,
                run_.end_datetime, ", ".join((str(i) for i in att_conf_ids)))

            values: List[int] = [v[0] for v in engine.execute(sql).fetchall()]

            for value in values:
                yield int(value)

    return list(get_values(query, run_model))


@cache.memoize(timeout=CACHE_TIMEOUT_SEC)
def _get_attrs_for_params(domain: str, family: str, member: str, name: str) -> List[Tuple[int, int]]:
    engine: Engine = db.get_engine(app.server, 'hdbpp')

    return list(engine.execute("""
        SELECT DISTINCT att_conf_data_type_id, att_conf_id
        FROM att_conf
        WHERE domain = "{}" AND family = "{}" AND member = "{}" AND name = "{}";
    """.format(domain, family, member, name)).fetchall())


def get_values(
        att_conf_data_type_id: int, att_conf_id:
        int, period: int, run: int) -> Dict[int, List[Tuple[datetime, int]]]:
    engine: Engine = db.get_engine(app.server, 'hdbpp')
    data_type: AttConfDataType = db.session.query(
            AttConfDataType).filter(AttConfDataType.att_conf_data_type_id == att_conf_data_type_id).first()
    run_model = _get_run(period, run)
    table_name = 'att_' + data_type.data_type

    if 'scalar' in data_type.data_type:
        sql = """
            SELECT data_time, value_r
            FROM {}
            WHERE (data_time BETWEEN "{}" AND "{}") AND att_conf_id = {};
        """.format(
            table_name,
            run_model.start_datetime,
            run_model.end_datetime, att_conf_id)
        return {0: engine.execute(sql).fetchall()}
    elif 'array' in data_type.data_type:
        sql = """
                    SELECT idx, data_time, value_r
                    FROM {}
                    WHERE (data_time BETWEEN "{}" AND "{}") AND att_conf_id = {};
                """.format(
            table_name,
            run_model.start_datetime,
            run_model.end_datetime, att_conf_id)

        data = engine.execute(sql).fetchall()

        data_dict = {}
        for entry in data:
            if entry[0] not in data_dict:
                data_dict[entry[0]] = []
            data_dict[entry[0]] += [(entry[1], entry[2]),]

        return data_dict


@cache.memoize(timeout=CACHE_TIMEOUT_SEC)
def initialize_domains(period: int, run: int) -> List[DomainEntry]:
    """Get all available domains from database."""
    attrs = _get_run_attrs(period, run)
    print("here")
    query = db.session.query(AttConf.domain) \
        .filter(text("att_conf_id in ({})".format(", ".join(str(v) for v in attrs)))).distinct()
    return [
        {'label': v[0], 'value': v[0]}
        for v in query]