import os
basedir = os.path.abspath(os.path.dirname(__file__))



class Config:
    SECRET_KEY = os.getenv('SECRET_KEY' 'SomeSecret')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
   # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    DEBUG = True
    SECRET_KEY = 'RandomSecret'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://sourdoughadmin@sourdoughmonitor01:ClintYeastwood2019@sourdoughmonitor01.mysql.database.azure.com/sourdoughmonitor01'#os.getenv('SQLALCHEMY_DATABASE_URI', 'mysql://sourdoughadmin@sourdoughmonitor01:ClintYeastwood2019@sourdoughmonitor01.mysql.database.azure.com/sourdoughmonitor01')
    DEBUG = False
    SECRET_KEY = 'SecretKeyisSecret' #  os.getenv('SECRET_KEY', 'SomeSecret')

class TestConfig(Config):
    pass


config = {'development': DevelopmentConfig,
          'production': ProductionConfig}