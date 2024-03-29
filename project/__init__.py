from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


_db = SQLAlchemy()

def create_app():
  app = Flask(__name__)
  
  app.config['SECRET_KEY'] = 'secret_key'
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jello.db'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  _db.init_app(app)

  login_manager = LoginManager()
  login_manager.login_view = 'auth.login'
  login_manager.init_app(app)

  from .models import User
  @login_manager.user_loader
  def load_user(identification):
    return User.query.get(int(identification))

  from .home import home as home_blueprint
  app.register_blueprint(home_blueprint)

  from .auth import auth as auth_blueprint
  app.register_blueprint(auth_blueprint)
  
  return app









