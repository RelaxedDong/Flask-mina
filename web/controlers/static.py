#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/22 20:40

from flask import Blueprint,send_from_directory

from application import app

route_static = Blueprint('static',__name__)
@route_static.route('/<path:filename>')
def index(filename):
    return send_from_directory(app.root_path+'/web/static/',filename)