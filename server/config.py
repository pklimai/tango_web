CACHE_TIMEOUT_SEC = 300
INITIAL_RUN_PERIOD = None
INITIAL_RUN_NUMBER = None

HOST = "0.0.0.0"
PORT = 8050
DEBUG = False

BMN_CONNECTION = "postgresql://db_reader:reader_pass@nc13.jinr.ru/bmn_db"
HDBPP_CONNECTION = "mysql+pymysql://tango:tangompd@10.18.11.66/hdbpp"
#HDBPP_CONNECTION = "postgresql://grafana:grafana@10.18.86.81:5000/hdb"

# Use for lab testing
# HDBPP_CONNECTION = "mysql+pymysql://user:user_pass@localhost/hdbpp"
# BMN_CONNECTION = "postgresql://user:user_pass@localhost/bmn_db"

ALIASES = [
    {
        'name': 'hall sensor',
        'param': dict(domain="mpd", family="bmn", member="adc_bman_beam", name="ch1")
    },
    {
        'name': 'gem trip',
        'param': dict(domain="mpd", family="gem", member="wiener_hv", name="trip")
    },
    {
        'name': "gem u",
        'param': dict(domain="mpd", family="gem", member="wiener_hv", name="u")
    },
]

try:
    from .config_local import *
except ModuleNotFoundError:
    pass

