import requests

from .config import TANGO_BASE_API_URL

class TangoApiReader:

    @staticmethod
    def get_domains():
        return requests.get(f"{TANGO_BASE_API_URL}/domains").json()

    @staticmethod
    def get_families(domain):
        return requests.get(f"{TANGO_BASE_API_URL}/families?domain={domain}").json()

    @staticmethod
    def get_members(domain, family):
        return requests.get(f"{TANGO_BASE_API_URL}/members?domain={domain}&family={family}").json()

    @staticmethod
    def get_names(domain, family, member):
        return requests.get(f"{TANGO_BASE_API_URL}/names?domain={domain}&family={family}&member={member}").json()

    @staticmethod
    # @utils.monitor_results
    def get_graph_data(domain, family, member, name, start_datetime, end_datetime):
        return requests.get(f"{TANGO_BASE_API_URL}/attdata?domain={domain}&family={family}&member={member}&name={name}&start_datetime={start_datetime}&end_datetime={end_datetime}").json()

