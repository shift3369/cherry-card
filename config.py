import os


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = '0c7df44b935f4e42499390690ab528d0'
    SECRET_KEY = '33f4fadaf33206cdc82e868ecf803fad'
    SQLALCHEMY_DATABASE_URI = os.environ['CHERRY_CARD_DATABASE_URI']


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
