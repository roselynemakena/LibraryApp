from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate



from configmodule import app_config
lm = LoginManager()

# app.config.from_object('configmodule.DevelopmentConfig')
db = SQLAlchemy()
def create_app(config_name):
	app = Flask(__name__, instance_relative_config=True)
	if not config_name:
		app.config.from_object(app_config['development'])

	else:
		app.config.from_object(app_config[config_name])
	app.config.from_pyfile('configmodule.py')
	db.init_app(app)

	#add login functionality
	lm.init_app(app)
	lm.login_message = "Please login to access this page"
	lm.login_view = "auth.login"

	migrate = Migrate(app, db)
	from app import models

	from .admin import admin as admin_blueprint
	app.register_blueprint(admin_blueprint, url_prefix='/admin')

	from .auth import auth as auth_blueprint
	app.register_blueprint(auth_blueprint)

	from .home import home as home_blueprint
	app.register_blueprint(home_blueprint)

	return app