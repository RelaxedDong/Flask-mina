#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/22 19:46

class Base_setting(object):
    DEBUG = True
    AUTH_COOKIE_NAME = 'mooc_food'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/food_db?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SERVER_PORT = 5000
    #过滤url
    IGNORE_URLS = [
        '/user/login/'
    ]
    IGNORE_CHECK_LOGIN_URLS = [
        'static',
        '/favicon.ico'
    ]


class Local_setting(Base_setting):
    pass

class Production_setting(Base_setting):
    DEBUG = False
