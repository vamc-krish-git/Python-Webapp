from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/green')
def green():
    print("This is green..")
    return render_template('green.html')

@app.route('/blue')
def blue():
    print("This is Blue..")
    return render_template('blue.html')

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port="5000")

# This is Feature1 on Feature1 Branch
# This is Second Commit to the Feature1 Branch

# This is for Demo wasdasd