from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


from configmodule import app_config

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


	return app