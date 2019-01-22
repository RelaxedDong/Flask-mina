#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/22 19:22
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from config import settings
import os

class Application(Flask):
    def __init__(self,import_name,**kwargs):
        super(Application, self).__init__(import_name,**kwargs)
        self.config.from_object(settings.Local_setting)
        db.init_app(self)

db = SQLAlchemy()
app = Application(__name__,template_folder=os.getcwd()+'/web/templates',root_path=os.getcwd(),static_folder=None)
manager  = Manager(app)

#函数模板
from common.libs.UrlManager import UrlManager
app.add_template_global(UrlManager.buildStaticUrl,"buildStaticUrl")
app.add_template_global(UrlManager.buildUrl,"buildUrl")