from flask import Flask, render_template, flash , redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError, Email

from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.secret_key = 'axfkjsadbhfkj'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'

db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

class LoginForm(FlaskForm):
    user_name = StringField("Username", validators=[InputRequired(), Length(min=4, max=150)])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=6)])
    submit = SubmitField("Login")

class RegistrationForm(FlaskForm):
    user_name = StringField("Username", validators=[InputRequired(), Length(min=4, max=150)])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=6)])
    confirm_password = PasswordField("Confirm Password", validators=[InputRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField("Register")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256')
        new_user = User(user_name=form.user_name.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash("Registration successful. Please log in.", "success")
        return redirect(url_for('login'))
    
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(user_name=form.user_name.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash("Login successful!", "success")
            return redirect(url_for('dashboard'))
        flash("Invalid username or password.", "danger")
    return render_template('login.html', form=form)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', user_name=current_user.user_name)
    
if __name__ == '__main__':

    with app.app_context():
        db.create_all()
    
    app.run(
        debug = True,
        port = 8989
    )