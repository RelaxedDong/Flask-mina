#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/22 19:56

from flask import Blueprint,render_template,request,jsonify
from common.models.user import User
route_user = Blueprint( 'user_page',__name__ )

@route_user.route( "/login/" ,methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template( "user/login.html" )
    else:
        req = request.values
        resp = {'code':200,'msg':'登陆成功','data':{}}
        login_name = req['login_name'] if 'login_name' in req else ''
        login_pwd = req['login_pwd'] if 'login_pwd' in req else ''
        if login_name is None or len(login_name)<1:
            resp['code'] = -1
            resp['msg'] = '请输入正确的用户名~'
            return jsonify(resp)
        if login_pwd is None or len(login_pwd) < 1:
            resp['code'] = -1
            resp['msg'] = '请输入正确的密码~'
            return jsonify(resp)
        user_info = User.query.filter_by(login_name = login_name).first()
        if not user_info:
            resp['code'] = -1
            resp['msg'] = '请输入正确的用户名和密码~'
            return jsonify(resp)
        else:
            return '登陆成功'

@route_user.route( "/edit/" )
def edit():
    return render_template( "user/edit.html" )

@route_user.route( "/reset-pwd/" )
def resetPwd():
    return render_template( "user/reset_pwd.html" )