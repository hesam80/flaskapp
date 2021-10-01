import os, requests
import random
from flask import Flask, flash, redirect, render_template, request, url_for, abort


app = Flask(__name__)


@app.route('/')
def view():
    """Return a friendly HTTP greeting."""
    firstmessage = "It's redeployedd Wow how it's Beautiful!"
    congramessage="Congratulations, you successfully deployed a container image to Cloud Run!"
    """Get Cloud Run environment variables."""
    service = os.environ.get('K_SERVICE', 'Unknown service')
    revision = os.environ.get('K_REVISION', 'Unknown revision')
    num=random.randint(1,12)
    hitt= num*2
    return render_template('index.html',num=num,hit=hitt,congmsg=congramessage,Service=service,Revision=revision,firstmsg=firstmessage)


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)

@app.route("/indexx")
def indexx():
	

    return render_template("indexx.html")
 
#Define 2nd Route and Content
@app.route("/success", methods = ['POST'])
def success():
  
  height=request.form["tool"]
  vazn = request.form["arz"]
  num=random.randint(1,12)
  return render_template('success.html', hit=height , number=num , vazn=vazn)
 
@app.route('/resultst')
def resultst():
	num=random.randint(1,12)
	return render_template('resultst.html', number=num)


if __name__ == '__main__':
    server_port = os.environ.get('PORT', '80')
    app.run(debug=True)