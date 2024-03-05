from flask import Blueprint

#สร้าง Blueprint เพื่อแยกการใช้งาน router: main
main = Blueprint('main', __name__)

#ดึงฟังชั่นใน routes.py มาใช้งาน
from app.main import routes