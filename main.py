import os
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email


app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.secret_key = os.environ.get("SECRET")


class NewsletterSignUpForm(FlaskForm):
    email = StringField('Your E-mail', validators=[DataRequired(), Email()])
    name = StringField('Your Name', validators=[DataRequired(), Length(min=2, max=50)])
    submit = SubmitField('Sign Up')


@app.route("/", methods=["GET", "POST"])
def home():
    newsletter_form = NewsletterSignUpForm()
    if newsletter_form.validate_on_submit():
        print(newsletter_form.email)
        print(newsletter_form.name)
        return redirect(url_for('home'))
    return render_template("index.html", form=newsletter_form)



if __name__ == '__main__':
    app.run(debug=True)
