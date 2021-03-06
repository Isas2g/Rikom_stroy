from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators = [ DataRequired() ])
    password = PasswordField('Пароль', validators = [ DataRequired() ])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')
    

    
    
class RegistrationForm(FlaskForm):
    username = StringField( 'Имя пользователя', validators = [ DataRequired() ] )
    email = StringField( 'Email', validators = [ DataRequired() ] )
    password = PasswordField('Пароль', validators = [ DataRequired() ] )
    password2 = PasswordField('Повторите пароль', validators = [DataRequired(), EqualTo('password')])
    wish = StringField('Ваше желание', validators = [ DataRequired() ])
    submit = SubmitField('П')
    
    
    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')
    
    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')
            