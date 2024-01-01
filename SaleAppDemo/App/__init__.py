from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = '@#$%^&#@$%^$%^&*@#$%^&43567*#$%^&*'
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:%s@localhost/saledb1?charset=utf8mb4' % quote('Nhatcuong123@')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"] = 6    #Sô phần tử trong trang là 6

db = SQLAlchemy(app=app)
login = LoginManager(app=app)

import cloudinary

cloudinary.config(
    cloud_name="dpizftz60",
    api_key="863397263737332",
    api_secret="KMyyLVw-qbQ950g_UmtGOR655XE"
)