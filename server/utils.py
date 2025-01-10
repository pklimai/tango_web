from time import mktime
from datetime import datetime
from typing import Union, List, Iterable, Tuple, Dict

from dateutil.parser import parse as tparse
from sqlalchemy import and_, text

from server import cache, db, app
from server.config import CACHE_TIMEOUT_SEC
from server.orm.bmn import Run
from server.tango_api_reader import TangoApiReader

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
def get_available_runs():
    with app.server.app_context():
        available_runs = {}
        for run in db.session.query(Run):
            if run.run_period.period_number not in available_runs:
                available_runs[run.run_period.period_number] = []
            available_runs[run.run_period.period_number].append(run.run_number)
        return [dict(period=r, numbers=available_runs[r]) for r in sorted(available_runs.keys(), reverse=True)]


@cache.memoize(timeout=CACHE_TIMEOUT_SEC)
def get_run(period: int = None, run: int = None) -> Union[Run, None]:
    if period is None or run is None:
        return None
    else:
        return db.session.query(Run) \
            .filter(and_(Run.period_number == period, Run.run_number == run)).first()


@cache.memoize(timeout=CACHE_TIMEOUT_SEC)
def _get_available_attrs():
    domains: List[str] = TangoApiReader.get_domains()
    result = {d: {} for d in domains}

    for domain in domains:
        families = TangoApiReader.get_families(domain)
        result[domain] = {f: {} for f in families}

        for family in families:
            members = TangoApiReader.get_members(domain, family)
            result[domain][family] = {m: {} for m in members}

            for member in members:
                names =  TangoApiReader.get_names(domain, family, member)
                result[domain][family][member] = names

    return result


@cache.memoize(timeout=CACHE_TIMEOUT_SEC)
def get_values_from_api(domain, family, member, name, start_dt, end_dt):
    return TangoApiReader.get_graph_data(domain, family, member, name, start_dt, end_dt)
