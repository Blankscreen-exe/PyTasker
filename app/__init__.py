from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_debugtoolbar import DebugToolbarExtension
from config import config_map

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
mail = Mail()
jwt = JWTManager()
toolbar = DebugToolbarExtension()
limiter = Limiter(key_func=get_remote_address)

def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config_map[config_name])

    # Init extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    mail.init_app(app)
    jwt.init_app(app)
    CORS(app)
    limiter.init_app(app)
    toolbar.init_app(app)
    
    from app import models
    
    # Register routes or blueprints
    from .routes import index_bp
    app.register_blueprint(index_bp)
    
    from app.auth import auth_bp
    app.register_blueprint(auth_bp)

    return app
