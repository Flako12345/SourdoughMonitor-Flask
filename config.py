import os
basedir = os.path.abspath(os.path.dirname(__file__))


## See configuration options in Flask by Miguel Grinberg
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY') or 'SomeSecret'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    DEBUG = True

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    DEBUG = False

class TestConfig(Config):
    pass


config = {'development': DevelopmentConfig,
          'production': ProductionConfig}