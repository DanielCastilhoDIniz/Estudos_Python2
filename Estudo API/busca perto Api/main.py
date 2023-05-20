from flask import Flask
from flask import render_template, redirect, url_for, flash, request, abort

from forms import FormCep
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


app = Flask(__name__)
app.config['SECRET_KEY'] = 'chave_secreta'


@app.route('/home', methods=['GET', 'POST'])
def home():

    form = FormCep()

    if form.validate_on_submit():
        cep = form.cep.data

        return render_template('index.html', cep=cep)

    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
