import os

DEBUG = True
SECRET_KEY = os.urandom(24)

HOSTNAME = '192.168.1.9'
PORT = '3306'
DATABASE = 'pcmp1'
USERNAME = 'root'
PASSWORD = '254562'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI