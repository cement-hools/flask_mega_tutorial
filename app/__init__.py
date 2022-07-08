from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app.errors import bp as errors_bp
from app.auth import bp as auth_bp
from config import Config


app.register_blueprint(errors_bp)
app.register_blueprint(auth_bp, url_prefix='/auth')

login = LoginManager()
login.login_view = 'login'

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

from app import routes, models
