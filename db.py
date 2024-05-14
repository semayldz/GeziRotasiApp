from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from app import app

db = SQLAlchemy(app)
login = LoginManager(app)

login.login_view = 'login'  #giriş yapmamış kullanıcıları log in sayfasına yönlendirecek
login.login_message_category = 'info'