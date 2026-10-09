from flask import Flask, render_template, request
import mysql.connector
app = Flask(__name__)
import re
@app.route('/login', methods=['GET','POST'])
def login():
    msg=''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:

        username = request.form['username']
        password = request.form['password']
        mydb = mysql.connector.connect(
        host="remotemysql.com",
        user="Rz8hqnldk4",
        password="nd0wK03xe0",
        database="Rz8hqnldk4"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM LoginDetails WHERE Name = %s AND Password = %s", (username, password))
        account = mycursor.fetchone()
        if account:
            print('login success')
            name = account[1]
            id = account[0]
            msg = 'Logged in Successfully'
            print('login successful!')
            return render_template('welcomepage.html', msg=msg, name=name, id=id)
        else:
            msg = 'incorrect Credentials. Kindly check'
            return render_template('loginpage.html', msg=msg)
    else:
        return render_template('loginpage.html')

def register():
    msg = ''
    if request.method == 'POST' and username in request.form and password in request.form and email in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        mydb = mysql.connector.connect(
            host='remoteysql.com',
            user='Rz8hqnlk4',
            password='nd6wK03xe0',
            database='Rz8hqnlk4'
        )
        mycursor = mydb.cursor()
        print(username)
        mycursor.execute('SELECT * FROM LoginDetails WHERE Name = %s AND Email_id = %s', (username, email))
        account = mycursor.fetchone()
        print(account)
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'^[^\d]*@[^\d]*\.\.[^\d]*$', email):
            msg = 'Invalid email address!'
        elif not re.match(r'(A-Za-z0-9)+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = "Kindly fill the details!"
        else:
            mycursor.execute('INSERT INTO LoginDetails VALUES (NULL, %s, %s, %s)', (username, password, email))
            mydb.commit()
            msg = 'Your registration is successful'
            name = username
            return render_template('index.html', msg=msg, name=name)
    elif request.method == 'POST':
        msg = 'Kindly fill the details!'
        return render_template('registration.html', msg=msg)
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)''')
    conn.commit()
    conn.close()
    
if __name__ == '__main__':
    init_db() # Initialize the database if it doesn't exist
    app.run(debug=True)
