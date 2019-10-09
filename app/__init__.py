from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
import os
from config import config
"""
basedir = os.path.abspath(os.path.dirname(__file__))
uri = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisverysecret'
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

"""
"""
migrate = Migrate(app, db)

"""
login_manager = LoginManager()
login_manager.login_view = 'auth.login'


db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    from .api import api as api_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app

