import os
basedir = os.path.abspath(os.path.dirname(__file__))



class Config:
    SECRET_KEY = os.getenv('SECRET_KEY' 'SomeSecret')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_SIZE = os.getenv('SQLALCHEMY_POOL_SIZE', 119)

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    DEBUG = True
    SECRET_KEY = 'RandomSecret'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY')

class TestConfig(Config):
    pass


config = {'development': DevelopmentConfig,
          'production': ProductionConfig}