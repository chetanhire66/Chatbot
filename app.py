from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from Chatbot import gimini

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hostale.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Sql(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    history = db.Column(db.String(100))

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        text = request.form['text']
        history_text = gimini(text)  # get response
        data = Sql(history=history_text)
        db.session.add(data)
        db.session.commit()
        return redirect('/')  # avoid resubmission
    
    all_data = Sql.query.all()
    return render_template('home.html', history=all_data)
@app.route('/delete/<int:id>')
def delete(id):
    delete = Sql.query.get_or_404(id)
    db.session.delete(delete)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
