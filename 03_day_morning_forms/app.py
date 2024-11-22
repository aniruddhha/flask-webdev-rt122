from flask import Flask, render_template, request, url_for, redirect, flash

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length


app = Flask(__name__)
app.secret_key = "ajasfhj"

class ContactForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(message="Invalid email address")])
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=10, message="Message must be at least 10 characters long")])
    submit = SubmitField('Submit')


@app.route('/form', methods = ['GET', 'POST'])
def form():
    form = ContactForm()
    if form.validate_on_submit():  # Validates form on POST
        email = form.email.data
        message = form.message.data
        flash(f"Message sent successfully by {email}!", "success")
        return render_template('success.html')  # Redirect to prevent form resubmission

    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug = True, port = 8989)

