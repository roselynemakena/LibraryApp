class Config(object):
	DEBUG = False


class ProductionConfig(Config):
    DEBUG = False
    DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
    DEBUG = True
    MAKENA = "roselyne"
    SQLALCHEMY_ECHO = True

class TestingConfig(Config):
    TESTING = True

app_config = {
	'development' : DevelopmentConfig,
	'production': ProductionConfig
}