import os

SECRET_KEY = "supersecret"
JWT_ALGORITHM = "HS256"
JWT_EXPIRATION_HOURS = 1

# Rate Limiting
RATE_LIMIT_LOGIN = "3 per minute"

# Email
EMAIL_FROM = "huxhron@gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
EMAIL_APP_PASSWORD = "muxwxqiykynjsery"

# DB
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, '../instance/users.db')}"
SQLALCHEMY_TRACK_MODIFICATIONS = False