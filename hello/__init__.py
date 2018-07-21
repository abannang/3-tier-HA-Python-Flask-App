from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required

app = Flask(__name__)
app.config.from_object('hello.config')

login_manager = LoginManager()
login_manager.init_app(app)

db = SQLAlchemy(app)
db_connection = db.engine.connect()
import hooks
import models
import views
