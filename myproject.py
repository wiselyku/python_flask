from flask import Flask,render_template, request
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'sysbench-test.cxanpzc7bsex.us-west-2.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'wisely96'
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)



@app.route("/ToDo")
def listall():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM ToDoList;')
    data = cursor.fetchall()
    return render_template("base.html",todo_list=data)
   ## return data

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello Flask!</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
