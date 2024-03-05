from flask import Flask

#ดึงค่า Config มาใช้
from config import Config
# ดึง extensions มาใช้
from app.extensions import socketio

# main Program ฟังชั่นแรหที่ถูกเรียกเมื่อรันเซิฟ
def create_app(config_class=Config):
    # กำหนดตัวแปล Flask
    app = Flask(__name__)
    # กำหนดคอนฟิก SECRET_KEY
    app.config['SECRET_KEY'] = config_class.SECRET_KEY

    # Initialize Flask extensions here
    socketio.init_app(app)

    # Register blueprints here
    from app.main import main as blueprint_main
    app.register_blueprint(blueprint_main)

    return app