import os

SQLALCHEMY_DATABASE_URI = 'mysql://root:@127.0.0.1:3306/cmdb'
SSHKEY_DATABASE_URI = 'mysql://root:anjuke@10.10.3.165:3306/sshkey?charset=utf8'
SQLALCHEMY_ENCODING = "utf-8"
SQLALCHEMY_ECHO = False
DEBUG = True

PRODUCT_CONFIG = '/home/www/config.py'
