from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///hostale.bd'

db = SQLAlchemy(app)
class sql(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

@app.route('/', methods=['GET','POST'])
def home():
    name=None
    if request.method=='POST':
        name = request.form['name']
    return render_template('home.html', name=name)

if __name__=='__main__':
    app.run(debug=True)