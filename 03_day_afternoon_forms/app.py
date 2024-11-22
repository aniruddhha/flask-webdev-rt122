from flask import Flask, render_template, request, flash, redirect, url_for

from flask_wtf import FlaskForm

from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length


app = Flask(__name__)
app.secret_key = 'askfdjskjfdv'

class ContactForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(message="Invalid email address")])
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=10, message="Message must be at least 10 characters long")])
    submit = SubmitField('Submit')

# @app.route('/', methods = ['GET', 'POST'])
# def contact():
#     return render_template('form.html')

# @app.route('/contact_submit', methods = ['POST'])
# def contact_submit():
#     email = request.form.get('email')
#     message = request.form.get('message')

#     print(f'Email {email}, Message {message}')

#     if not email or not message:
#         return render_template('error.html')
#         flash('Both Email and Message are mandetory')
#     # else:
#     #     flash('Thanks for submitting the form')
#     return render_template('success.html')

@app.route('/form', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    # if form.validate_on_submit():  # Validates form on POST
    #     email = form.email.data
    #     message = form.message.data

    #     flash(f"Message sent successfully by {email}!", "success")

    #     return redirect(url_for('form'))  # Redirect to prevent form resubmission

    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(
        debug = True, 
        port = 8989
    )