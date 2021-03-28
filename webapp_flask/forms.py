####################################################################################################
#####                   Module Imports                                                         #####
####################################################################################################

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo

####################################################################################################
#####                   Forms                                                                  #####
####################################################################################################

#    class RegistrationForm(FlaskForm):
#        username = StringField('Username',
#                                validators=[DataRequired(), Length(min=2, max=20)])
#        email = StringField('Email',
#                            validators=[DataRequired(), Email()])
#        password = PasswordField('Password', validators=[DataRequired()])
#        confirm_password = PasswordField('Confirm Password',
#                                        validators=[DataRequired(), EqualTo('password')])
#        submit = SubmitField('Sign Up')
#
#    class LoginForm(FlaskForm):
#        email = StringField('Email',
#                            validators=[DataRequired(), Email()])
#        password = PasswordField('Password', validators=[DataRequired()])
#        remember = BooleanField('Remember Me')
#        submit = SubmitField('Login')

class ProductSearchForm(FlaskForm):
    search = StringField('Search')
    choices = [('Name_Alphabet', 'Name (A -> Z)'),
                ('Name_Reverse_Alphabet', 'Name (Z -> A)'),
                ('Quantity_High', 'Quantity (High -> Low)'),
                ('Quantity_Low', 'Quantity (Low -> High)'),
                ('Price_High', 'Price (High -> Low)'),
                ('Price_Low', 'Price (Low -> High)')]
    select = SelectField('Sort by:', choices=choices)
    submit = SubmitField('Enter search')