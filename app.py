import os, requests
import random , sqlite3
from flask import Flask, flash, redirect, render_template, request, url_for, abort, redirect
import models as dbHandler

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home():
    """Return a friendly HTTP greeting."""
    firstmessage = "It's redeployedd Wow how it's Beautiful!"
    congramessage="Congratulations, you successfully deployed a container image to Cloud Run!"
    """Get Cloud Run environment variables."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        dbHandler.insertUser(username, password)
        users = dbHandler.retrieveUsers()
        return render_template('index.html',congmsg=congramessage ,firstmsg=firstmessage, users=users)
    else:
            error = 'Invalid username/password'
            redirect(url_for('register'))
   
    return render_template('index.html',congmsg=congramessage ,firstmsg=firstmessage, error=error)
@app.route('/register')
def register():
	
	return render_template('register.html')

@app.route('/login')
def login():

    return render_template('login.html')

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '80')
    app.run(debug=True)