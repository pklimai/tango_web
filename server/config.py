CACHE_TIMEOUT_SEC = 300
INITIAL_RUN_PERIOD = None
INITIAL_RUN_NUMBER = None

HDBPP_CONNECTION = "mysql+pymysql://user:user_pass@localhost/hdbpp"
BMN_CONNECTION = "postgresql://user:user_pass@localhost/bmn_db"

try:
    from .config_local import *
except ModuleNotFoundError:
    pass

