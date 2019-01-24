#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/22 19:22
from application import app
from web.controlers.index import route_index
from web.controlers.user.User import route_user
from web.controlers.account.Account import route_account
from web.controlers.finance.Finance import route_finance
from web.controlers.food.Food import route_food
from web.controlers.stat.Stat import route_stat
from web.controlers.member.Member import route_member
from web.controlers.static import *

'''拦截器'''
from web.interceptors.Authinterceptor import before_request

app.register_blueprint(route_index,url_prefix='/')
app.register_blueprint(route_user,url_prefix='/user')
app.register_blueprint(route_user,url_prefix='/user')
app.register_blueprint(route_static,url_prefix='/static')
app.register_blueprint(route_account,url_prefix='/account')
app.register_blueprint(route_food,url_prefix='/food')
app.register_blueprint(route_finance,url_prefix='/finance')
app.register_blueprint(route_stat,url_prefix='/stat')
app.register_blueprint(route_member,url_prefix='/member')