from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

migrate = Migrate(app, db)

class AppUser(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String(80), nullable = False)
    email = db.Column(db.String(100), unique = True, nullable = False)
    password = db.Column(db.String(100), nullable = False)


@app.route('/create')
def create():
    user1 = AppUser(
        user_name = 'abc',
        email = 'aaa@bb.com',
        password = '123Acn'
    )
    db.session.add(user1)

    user2 = AppUser(
        user_name = 'pqr',
        email = 'sss@tt.com',
        password = 'kjh654564'
    )
    db.session.add(user2)

    user3 = AppUser(
        user_name = 'ajfhgjhg',
        email = 'mnbmbn@tkjht.com',
        password = '76yfghvg'
    )
    db.session.add(user3)

    db.session.commit()
    return '<h1> User Created Successfully </h1>'

@app.route('/read')
def read():
    user = AppUser.query.filter_by(email = 'aaa@bb.com').first()
    return f' User Name {user.user_name}, Email {user.email}'

@app.route('/all')
def read_all():
    users = AppUser.query.all()
    return render_template('users.html', users = users)

@app.route('/update')
def update():
    user = AppUser.query.filter_by(email = 'aaa@bb.com').first()
    user.email = 'www@ppp.com'
    db.session.commit()

@app.route('/delete')
def delete():
    'Please Try Delete On your Own'

if __name__ == '__main__':
    with app.app_context():
        db.create_all() 

    app.run(
        debug = True,
        port = 8989
    )


