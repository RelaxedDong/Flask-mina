#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/22 19:22
from application import app,manager
from flask_script import Server
import www
manager.add_command("runserver",Server(host='127.0.0.1', port=app.config['SERVER_PORT'], use_debugger=app.config['DEBUG']))

def main():
    manager.run()

if __name__ == '__main__':
    try:
        import sys
        sys.exit( main())
    except Exception as e:
        import traceback
        traceback.print_exc()

