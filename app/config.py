import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '_something_that-is_hard_to_guess-i_think'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
