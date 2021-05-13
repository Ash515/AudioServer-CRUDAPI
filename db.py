from app import app
from flask_mysqldb import MySQLdb
mysql = MySQLdb()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'audioserver'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)