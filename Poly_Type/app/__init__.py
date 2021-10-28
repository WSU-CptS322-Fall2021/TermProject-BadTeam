from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_moment import Moment

db = SQLAlchemy()
moment = Moment()
login = LoginManager()
login.login_view = 'routes.index'

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.static_folder = config_class.STATIC_FOLDER 
    app.template_folder = config_class.TEMPLATE_FOLDER

    db.init_app(app)
    moment.init_app(app)
    login.init_app(app)

    from app.Controller.challengerRoutes import challenger_routes as challenger
    app.register_blueprint(challenger)

    from app.Controller.hostRoutes import host_routes as host
    app.register_blueprint(host)

    if not app.debug and not app.testing:
        pass
        # ... no changes to logging setup

    return app
