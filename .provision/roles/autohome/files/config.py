import os

SQLALCHEMY_DATABASE_URI = 'mysql://root:@127.0.0.1:3306/cmdb'
SSHKEY_DATABASE_URI = 'mysql://root:anjuke@10.10.3.165:3306/sshkey?charset=utf8'
SQLALCHEMY_ENCODING = "utf-8"
SQLALCHEMY_ECHO = False
DEBUG = True

PRODUCT_CONFIG = '/home/www/config.py'
#migrate
MIGRATE_DATABSE_URI ='mysql://root:cmdb_rw@127.0.0.1:3306/zeus?charset=utf8'
PARTS_MIGRATE_DATABASE_URI = 'mysql://root:admin@192.168.1.221:3306/IT?charset=utf8'
#openebula
VM_DATABASE_URI = 'mysql://opennebula:alubennepo123@10.10.8.35:3306/opennebula?charset=utf8'

#elasticsearc
ES_HOST="10.10.9.48"
ES_PORT=9200

# celery
BROKER_URL = 'redis://127.0.0.1:6379/0'

#ANSIBLE
ANSIBLE_BIZPATH = '/home/www/biz_ansible'
ANSIBLE_BIZCONFIG = '/home/www/biz_config'
ANSIBLE_BIZTEMP = '/home/www/biz_ansibletemp'
PYTHON_VPATH = '/home/www/virpython/bin/python'
ANSIBLE_PLAYBOOK = '/home/www/virpython/bin/ansible-playbook'

#ZABBIX API AUTH_URL
ZABBIX_API_URL_10 = 'http://zabbix10.corp.anjuke.com/api/fastApi.php'
ZABBIX_API_URL_20 = 'http://zabbix20.corp.anjuke.com/api/fastApi.php'

#SERVER PORT
SERVER_PORT = 5000

# oauth
AUTH_URL = 'https://auth.corp.anjuke.com/oauth/2.0'
AUTH_ID = 'nzl7lysmdgh3muzzrp9v'
AUTH_SECRET = 'upe56ihqknuoiev5feeem283zw7wxjra7edpkgjv'
SECRET_KEY = os.urandom(24)

# DB BACK PATH
BACKUP_PATH = '/home/www/cmdb_databack'

#IGNOREPATH
IGNOREPATH  = '^/$|^/user/follow|^/user/log*|^user/search|^/user/act*|^/static|^/cmdb/monitor|/cmdb/log|^/api/|^/logger'
#nginx path
NGINX_PATH = '/home/www/temp/'

#sendmail
SENDER = 'noreply-cmdb@anjuke.com'
SMTP_SERVER = 'smtp.anjuke.com'
USER_NAME = 'noreply-cmdb@anjuke.com'
PASSWORD = 'anjuke2014'
MAIL_TO = {
"pool_change_check":'bobxia@anjukeinc.com;Vincentguo@anjuke.com;pengxie@anjuke.com;xiaofanluo_h57@anjuke.com;jinbangyu@anjuke.com;jianqiangni@anjuke.com',
"pubkey_fail":'Vincentguo@anjuke.com;13774355074@139.com',
"pool_ratio":'Vincentguo@anjuke.com;bobxia@anjukeinc.com;Vincentguo@anjuke.com;pengxie@anjuke.com;xiaofanluo_h57@anjuke.com;jinbangyu@anjuke.com;jieqin@anjuke.com'
}
mail_receiver = 'bobxia@anjukeinc.com,Vincentguo@anjuke.com,pengxie@anjuke.com,xiaofanluo_h57@anjuke.com,jinbangyu@anjuke.com'

#REDIS
LOGGER_REDIS = {
	"HOST":'10.10.3.210',
	"PORT":6467
}

#zabbix info
ZABBIX10_URL = 'http://zabbix10.corp.anjuke.com/api_jsonrpc.php'
ZABBIX20_URL = 'http://zabbix20.corp.anjuke.com/api_jsonrpc.php'
ZABBIX_USER  = 'admin'
ZABBIX_PASS  = 'YWprX29wcwo='
ZABBIX_LOG_DIR   = "/var/log/zabbix"

#domain
DOMAIN = 'http://127.0.0.1:5000'

#host_apply approver
HOST_APPROVER = ['bobxia','pengxie','vincentguo',' xiaofanluo_h57']