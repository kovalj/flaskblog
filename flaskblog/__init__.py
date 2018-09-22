import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


app = Flask(__name__)
app.config['SECRET_KEY'] = 'b7c803efad40e8b6cbdcecdc4b42eb5a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = '9ec9acc47ccd13'  #os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = 'ccc8479f4c5c4d'  #os.environ.get('EMAIL_PASS')
mail = Mail(app)


from flaskblog import routes
