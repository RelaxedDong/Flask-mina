#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/22 19:56

from flask import Blueprint
from common.libs.helpler import ops_render
from common.models.user import User
route_account = Blueprint( 'account_page',__name__ )

@route_account.route( "/index" )
def index():
    resp_data = {}
    users = User.query.order_by(User.uid.desc()).all()
    resp_data['list'] = users
    return ops_render( "account/index.html",resp_data )

@route_account.route( "/info" )
def info():
    return ops_render( "account/info.html" )

@route_account.route( "/set" )
def set():
    return ops_render( "account/set.html" )
