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
    user_name = db.Column(db.String(80), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)

    def __repr__(self):
        return f'<AppUser {self.user_name}>'  # Optional for human-readable representation

@app.route('/')
def index():
    users = AppUser.query.all()
    # return f'<h1>Welcome!</h1><p>Here are some users (if any):</p><ul>{"".join([f"<li>{user}</li>" for user in users])}</ul>'
    return render_template('users.html', users = users)


@app.route('/single')
def single_user():
    user = AppUser.query.filter_by(user_name='abc').first()
    return f'User Name {user.user_name}, Email {user.email}'

@app.route('/create')
def create():
    new_user = AppUser(
        user_name = 'abc',
        email = 'aaa@@bb.co,'
    )

    db.session.add(new_user)
    db.session.commit()

    return 'User Created Successfully'

@app.route('/update')
def update():
    user = AppUser.query.filter_by(user_name='abc').first()
    user.user_name = 'qqq'
    db.session.commit()
    return f'User Name {user.user_name}, Email {user.email}'

@app.route('/delete')
def delete():
    'Complete the code'

if __name__ == '__main__':

    with app.app_context():
        db.create_all()

    app.run(
        debug = True, 
        port = 8989
    )