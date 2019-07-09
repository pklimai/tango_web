import dash
import dash_bootstrap_components as dbc
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy

from server.config import HDBPP_CONNECTION, BMN_CONNECTION

__external_stylesheets = [
    dbc.themes.BOOTSTRAP
]

app = dash.Dash(__name__, external_stylesheets=__external_stylesheets)

app.server.config['SQLALCHEMY_BINDS'] = {
    "hdbpp": HDBPP_CONNECTION,
    "bmn": BMN_CONNECTION
}
app.server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app.server)
cache = Cache(app.server, config={'CACHE_TYPE': 'simple'})