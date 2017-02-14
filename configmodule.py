class Config(object):
	DEBUG = False


class ProductionConfig(Config):
    DEBUG = False
    DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
    DEBUG = True
    MAKENA = "roselyne"
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://admin:root@localhost/library'


class TestingConfig(Config):
    TESTING = True

app_config = {
	'development' : DevelopmentConfig,
	'production': ProductionConfig

}