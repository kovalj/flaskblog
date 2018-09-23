import os


class Config:
    SECRET_KEY = 'b7c803efad40e8b6cbdcecdc4b42eb5a'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USE_TLS = True
    MAIL_USERNAME = '9ec9acc47ccd13'  # os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = 'ccc8479f4c5c4d'  # os.environ.get('EMAIL_PASS')
