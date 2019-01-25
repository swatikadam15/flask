from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import Required
from app import app
app.config['SECRET_KEY'] = 'hard to get string'
class NameForm(Form):
    name = TextField('what is your name?' ,validators = [ Required() ])
    

