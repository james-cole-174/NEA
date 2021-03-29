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
    choices = [('11', 'Name (A -> Z)'), # the first part identifiies the column to search by, the second part specifies if its ascending or descending
                ('10', 'Name (Z -> A)'),
                ('20', 'Quantity (High -> Low)'),
                ('21', 'Quantity (Low -> High)'),
                ('30', 'Price (High -> Low)'),
                ('31', 'Price (Low -> High)')]
    select = SelectField('Sort by:', choices=choices)
    submit = SubmitField('Enter search')

class OrderSearchForm(FlaskForm):
    choices = [('10', 'ID (High -> Low)'), # the first part identifiies the column to search by, the second part specifies if its ascending or descending
                ('11', 'ID (Low -> High)'),
                ('21', 'Status (A -> Z)'),
                ('20', 'Status (Z -> A)'),
                ('30', 'Price (High -> Low)'),
                ('31', 'Price (Low -> High)')]
    select = SelectField('Sort by:', choices=choices)
    submit = SubmitField('Enter search')
