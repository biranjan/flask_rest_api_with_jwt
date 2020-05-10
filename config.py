import os
basedir = os.path.abspath(os.path.dirname(__file__))

dbuser = os.environ['DBUSER']
dbpass = os.environ['DBPASS']
dbhost = os.environ['DBHOST']
dbname = os.environ['DBNAME']

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
  



class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SECRET_KEY = 'super-secret'
    SQLALCHEMY_DATABASE_URI = f'postgresql://{dbuser}:{dbpass}@{dbhost}/{dbname}'  # os.environ['DATABASE_URL']
    #SQLALCHEMY_DATABASE_URI = "postgresql://username:password@localhost/database_name"



class TestingConfig(Config):
    TESTING = True