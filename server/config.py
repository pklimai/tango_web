CACHE_TIMEOUT_SEC = 300
INITIAL_RUN_PERIOD = None
INITIAL_RUN_NUMBER = None

HOST = "0.0.0.0"
PORT = 8050
DEBUG = False

BMN_UNICONDA_CONNECTION = "postgresql://db_reader:reader_pass@bmn-unidb.jinr.ru/uni_db"
TANGO_BASE_API_URL = "http://127.0.0.1:8000/tango_api/v1"  # If not running locally, override with config_local.py

# Use for lab testing
# BMN_UNICONDA_CONNECTION = "postgresql://user:user_pass@localhost/bmn_db"
# TANGO_BASE_API_URL = "http://127.0.0.1:8000/tango_api/v1"

ALIASES = [
    {
        'name': "event number",
        'param': dict(domain="daq", family="system", member="status", name="ev_number")
    },
    {
        'name': "temperature pir230e_1",
        'param': dict(domain="bmn", family="env", member="pir230e_1", name="temperature")
    },
    {
        'name': "temperature pir230e_3",
        'param': dict(domain="bmn", family="env", member="pir230e_3", name="temperature")
    },
]

try:
    from .config_local import *
except ModuleNotFoundError:
    pass
except ImportError:
    pass
