CACHE_TIMEOUT_SEC = 300
INITIAL_RUN_PERIOD = None
INITIAL_RUN_NUMBER = None

HOST = "0.0.0.0"
PORT = 8050
DEBUG = False

HDBPP_CONNECTION = "mysql+pymysql://user:user_pass@localhost/hdbpp"
BMN_CONNECTION = "postgresql://user:user_pass@localhost/bmn_db"

ALIASES = [
    {
        'name': "gem_hv",
        'param': dict(domain="mpd", family="gem", member="wiener_hv", name="u")
    },
    {
        'name': "batt_t",
        'param': dict(domain="bmn", family="daq", member="ups", name="batterytemperature")
    },
]

try:
    from .config_local import *
except ModuleNotFoundError:
    pass

