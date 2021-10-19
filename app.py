import os, requests
import random , sqlite3
from flask import Flask, flash, redirect, render_template, request, url_for, abort, redirect, session
from flask_session import Session
# from flask_session.__init__ import Session
import models as dbHandler

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/', methods=['POST', 'GET'])
def home():
    if not session.get("username"):
       # if not there in the session then redirect to the login page
        return redirect("/register")
    """Return a friendly HTTP greeting."""
    firstmessage = "It's redeployedd Wow how it's Beautiful!"
    congramessage="Congratulations, you successfully deployed a container image to Cloud Run!"
    """Get Cloud Run environment variables."""        
    
    error = 'please sign up user pass'
            #return redirect(url_for('register'))
    return render_template('index.html',congmsg=congramessage ,firstmsg=firstmessage, error=error)

@app.route('/result', methods=['POST','GET'])
def result():
    if not session.get("username"):
        # if not there in the session then redirect to the login page
        return redirect("/register")
    
    return render_template('result.html')



@app.route('/register', methods=['POST' , 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        session["username"] = request.form.get("username")
        dbHandler.insertUser(username, password)
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=["POST", "GET"])
def login():
    if session.get("username"):
        users = dbHandler.retrieveUsers()
        return render_template('login.html',users=users)
    return redirect(url_for('home'))

@app.route('/delete_user', methods=['POST'])
def delete_user():
    dbHandler.deleteUser(request.form['user_to_delete'])
    return redirect(url_for('logout'))

@app.route("/logout")
def logout():
    session["username"] = None
    return redirect("/")

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '80')
    app.run(host="0.0.0.0",debug=True)