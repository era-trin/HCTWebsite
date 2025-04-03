from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length, Email
import json


contactform = Blueprint('contactform',__name__)

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=10)])



@contactform.route('/', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        new_entry = {'name': name, 'email': email, 'message': message}
        
        with open('messages.json', 'a') as file:
            file.write(json.dumps(new_entry) + "\n")
        
        # validation
        if not name or not email or not message:
            flash('All fields are required!')
            return redirect(url_for('contactform.contact'))
       
        if len(name) < 2 or len(name) > 50:
            flash('Name must be between 2 and 50 characters.')
            return redirect(url_for('contactform.contact'))
       
        # if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        #     flash('Invalid email address.')
        #     return redirect(url_for('contact'))
       
        if len(message) < 5:
            flash('Message must be at least 10 characters long.')
            return redirect(url_for('contactform.contact'))

        # Add server-side processing or send email here
        flash('Thank you for submitting your message!')
        return redirect(url_for('contactform.contact'))
    return render_template('contact.html', form=form)