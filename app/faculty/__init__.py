from flask import Blueprint

#สร้าง Blueprint เพื่อแยกการใช้งาน router: main
faculty = Blueprint('faculty', __name__)

#ดึงฟังชั่นใน routes.py มาใช้งาน
from app.faculty import routes