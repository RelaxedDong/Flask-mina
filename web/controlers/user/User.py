#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/22 19:56

from flask import Blueprint,render_template,request,jsonify,make_response,redirect,g
import json
from application import db
from common.libs.helpler import ops_render
from common.libs.UrlManager import UrlManager
from common.models.user import User
from common.libs.user.UserService import UserService
from application import app
from wtforms.validators import Email

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
            resp['msg'] = '请输入正确的用户名和密码-1~'
            return jsonify(resp)
        if user_info.login_pwd != UserService.genePwd(login_pwd, user_info.login_salt):
            resp['code'] = -1
            resp['msg'] = "请输入正确的登录用户名和密码-2~~"
            return jsonify(resp)
        response = make_response(json.dumps({'code': 200, 'msg': '登录成功~~'}))
        response.set_cookie(app.config['AUTH_COOKIE_NAME'], '%s#%s' % (
            UserService.geneAuthCode(user_info), user_info.uid), 60 * 60 * 24 * 120)  # 保存120天
        return response

@route_user.route( "/edit/",methods=['GET','POST'] )
def edit():
    if request.method == 'GET':
        return ops_render( "user/edit.html" )
    req = request.values
    resp = {'code': 200, 'msg': '操作成功', 'data': {}}
    nickname = req['nickname'] if 'nickname' in req else ''
    email = req['email'] if 'email' in req else ''
    if nickname is None or len(nickname) <2:
        resp['code'] = -1
        resp['msg'] =  '姓名至少两个字符'
        return jsonify(resp)

    if email is None or len(email) < 2:
        resp['code'] = -1
        resp['msg'] = '请输入规范的邮箱'
        return jsonify(resp)

    user_info = g.current_user
    user_info.nickname = nickname
    user_info.email = email
    db.session.commit()
    return jsonify(resp)

@route_user.route( "/reset-pwd/",methods=['GET','POST'] )
def resetPwd():
    if request.method == 'GET':
        return ops_render( "user/reset_pwd.html" )
    req = request.values
    resp = {'code': 200, 'msg': '操作成功', 'data': {}}
    new_password = req['new_password'] if 'new_password' in req else ''
    old_password = req['old_password'] if 'old_password' in req else ''
    if old_password is None or len(old_password) <6:
        resp['code'] = -1
        resp['msg'] =  '请输入符合规范的原密码'
        return jsonify(resp)

    if new_password is None or len(new_password) < 6:
        resp['code'] = -1
        resp['msg'] = '请输入符合规范的新密码'
        return jsonify(resp)

    if old_password == new_password:
        resp['code'] = -1
        resp['msg'] = '新旧密码不能一致'
        return jsonify(resp)

    user_info = g.current_user
    user_info.login_pwd = UserService.genePwd(new_password,user_info.login_salt)
    db.session.commit()
    response = make_response(json.dumps(resp))
    response.set_cookie(app.config['AUTH_COOKIE_NAME'], '%s#%s' % (
        UserService.geneAuthCode(user_info), user_info.uid), 60 * 60 * 24 * 120)  # 保存120天
    return response


@route_user.route( "/logout" )
def logout():
    response = make_response(redirect(UrlManager.buildUrl("/user/login/")))
    response.delete_cookie(app.config['AUTH_COOKIE_NAME'])
    return response