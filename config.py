import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:6775@localhost/sunday'
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    pass
   

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:6775@localhost/sunday'
    SECRET_KEY = 'This_is_my_secret'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
} 