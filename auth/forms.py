from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import InputRequired, Email, Length, ValidationError


class RegisterForm(FlaskForm):
    username = StringField("Имя пользователя: ", validators=[InputRequired()])
    email = StringField("Email: ", validators=[Email()])
    password = PasswordField("Пароль: ", validators=[InputRequired(), Length(min=4, max=100)])
    confirm_password = PasswordField("Повторите пароль: ", validators=[InputRequired(), Length(min=4, max=100)])
    submit = SubmitField("Регистрация")

    def validate_confirm_password(self, field):
        if field.data != self.password.data:
            raise ValidationError("Пароли должны совпадать")


class LoginForm(FlaskForm):
    username = StringField("Имя пользователя: ", validators=[InputRequired()])
    password = PasswordField("Пароль: ", validators=[InputRequired(), Length(min=4, max=100)])
    remember = BooleanField("Запомнить", default=False)
    submit = SubmitField("Войти")
