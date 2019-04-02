import dash
from flask_sqlalchemy import SQLAlchemy

__external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=__external_stylesheets)

app.server.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://user:user_pass@localhost/hdbpp"
app.server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app.server)