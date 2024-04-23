from flask import Flask, render_template, request, session, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_oidc import OpenIDConnect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'

app.config['SECRET_KEY'] = '12345678##'  # Update with your own secret key
app.debug = True  # Enable debug mode

app.config['OIDC_CLIENT_SECRETS'] = 'client_secrets.json'
app.config['OIDC_COOKIE_SECURE'] = False
app.config['OIDC_CALLBACK_ROUTE'] = '/oidc/callback'
# app.config['OIDC_SCOPES'] = ['openid', 'email', 'profile']

oidc = OpenIDConnect(app)

@app.route('/')
@oidc.require_login
def index():
    if oidc.user_loggedin:
        return render_template('index.html')
    else:
        print("Login Error")
        return redirect(url_for('oidc.login'))

@app.route('/green')
def green():
    print("This is green..")
    return render_template('green.html')

@app.route('/oidc/callback')
def blue():
    print("This is Blue..")
    return render_template('blue.html')

@app.route('/gray')
def gray():
    print("This is Gray..")
    return render_template('gray.html')

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port="3000")

# This is Feature1 on Feature1 Branch
# This is Second Commit to the Feature1 Branch

# This is for Demo wasdasd
