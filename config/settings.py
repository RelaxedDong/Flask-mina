#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/22 19:46

class Base_setting(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/order?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SERVER_PORT = 5000

class Local_setting(Base_setting):
    pass

class Production_setting(Base_setting):
    DEBUG = False
