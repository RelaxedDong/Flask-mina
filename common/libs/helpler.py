#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/24 21:17
'''同意渲染方法'''
from flask import g,render_template

def ops_render(template,context = {}):
    if 'current_user' in g:
        context['current_user'] = g.current_user
    return render_template(template,**context)