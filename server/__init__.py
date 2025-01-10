import dash
import dash_bootstrap_components as dbc
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy

from server.config import BMN_UNICONDA_CONNECTION

__external_stylesheets = [
    dbc.themes.BOOTSTRAP
]

app = dash.Dash(__name__, external_stylesheets=__external_stylesheets)

app.server.config['SQLALCHEMY_BINDS'] = {
    "bmn": BMN_UNICONDA_CONNECTION
}
app.server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app.server)
cache = Cache(app.server, config={'CACHE_TYPE': 'simple'})