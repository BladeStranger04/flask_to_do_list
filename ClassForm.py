from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired


class Form(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = StringField('Пароль', validators=[DataRequired()])
    password_again = StringField('Подтвердите пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submitR = SubmitField('Зарегистрироваться')
    submitL = SubmitField('Авторизоваться')
