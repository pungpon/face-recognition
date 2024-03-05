from flask import Flask

#ดึงค่า Config มาใช้
from config import Config
# ดึง extensions มาใช้
from app.extensions import socketio

from .database import Database

# main Program ฟังชั่นแรหที่ถูกเรียกเมื่อรันเซิฟ
def create_app(config_class=Config):
    # กำหนดตัวแปล Flask
    app = Flask(__name__)
    # กำหนดคอนฟิก SECRET_KEY
    app.config['SECRET_KEY'] = config_class.SECRET_KEY
    
    # Initialize Database
    Database().init()

    # Initialize Flask extensions here
    socketio.init_app(app)

    # Register blueprints here
    # Register Main
    from app.main import main as blueprint_main
    app.register_blueprint(blueprint_main)
    
    # Register Faculty
    from app.faculty import faculty as blueprint_faculty
    app.register_blueprint(blueprint_faculty, url_prefix='/faculty')

    return app