from flask_socketio import SocketIO

#สร้าง ตัวแปล
socketio = SocketIO()

#ดึงฟังชั่นใน events.py มาใช้งาน
import app.events