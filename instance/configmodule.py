class Config(object):
	DEBUG = False


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgres://xkfnfnolmwtecu:97e92be31c16f530e1c9eae4065b67bbec563aaa7368e691fb5516e708f84578@ec2-107-20-191-76.compute-1.amazonaws.com:5432/ddkl07tsnsinfr'

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