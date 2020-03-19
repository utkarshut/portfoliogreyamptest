from app import app
from flaskext.mysql import MySQL

app.config['MYSQL_DATABASE_HOST'] = 'us-cdbr-iron-east-04.cleardb.net'
app.config['MYSQL_DATABASE_USER'] = 'bbe61b03d957b1'
app.config['MYSQL_DATABASE_PASSWORD'] = '66111f55'
app.config['MYSQL_DATABASE_DB'] = 'heroku_3fabd405f1a8d0f'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL()
mysql.init_app(app)
