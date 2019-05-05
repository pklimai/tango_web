import dash
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy

__external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=__external_stylesheets)

app.server.config['SQLALCHEMY_BINDS'] = {
    "hdbpp": "mysql+pymysql://user:user_pass@localhost/hdbpp",
    "bmn": "postgresql://user:user_pass@localhost/bmn_db"
}
app.server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app.server)
cache = Cache(app.server, config={'CACHE_TYPE': 'simple'})