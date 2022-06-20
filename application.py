# -*- coding: utf-8 -*-
# from flask import Flask
from  flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
import os
import pymysql


class Application( Flask ):
    def __init__(self,import_name , template_folder = None,root_path = None ):
        super( Application,self ).__init__( import_name ,template_folder = template_folder,root_path = root_path,static_folder = None)
        self.config.from_pyfile( 'config/base_setting.py' )
        # ops_config为在系统环境配置中的key，值为local
        if "ops_config" in os.environ:
            self.config.from_pyfile( 'config/%s_setting.py'%os.environ['ops_config'] )

        db.init_app( self )

# pymysql.install_as_MySQLdb()

# 创建连接数据库对ORM类表操作的对象
db = SQLAlchemy()

app = Application( __name__ ,template_folder = os.getcwd() + "/web/templates/",root_path = os.getcwd() )
manager = Manager( app )

'''
函数模板
'''
from common.libs.UrlManager import UrlManager
app.add_template_global(UrlManager.buildStaticUrl, 'buildStaticUrl')
app.add_template_global(UrlManager.buildUrl, 'buildUrl')
app.add_template_global(UrlManager.buildImageUrl, 'buildImageUrl')


