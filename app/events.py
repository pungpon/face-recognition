from flask_socketio import emit
from flask import request

# ดึง extensions มาใช้
from .extensions import socketio
# ดึง globals variable มาใช้
from app.globals import page_setting

#เมื่อมีการ เชื่อมต่อ หรือเปิดแท็บ ในที่กำหนดไว้ page_setting
@socketio.on("connect")
def handle_connect():
    print("Client connected!")

#เมื่อมีการ ยกเลิกเชื่อมต่อ หรือปิดแท็บ ในที่กำหนดไว้ page_setting
@socketio.on("disconnect")
def handle_disconnect():
    print("Client disconnect!")
    for i in page_setting:
        if request.sid == page_setting[i]["current_usage_id"]:
            page_setting[i]["current_usage_id"] = None
            page_setting[i]["current_usage"] = False

#เมื่อมีการเชื่อมต่อ จะมีการ emit จาก clients รับค่า data มาด้วย
@socketio.on("event")
def handle_myevent(data):
    # data คือ {"data": "ชื่อ อิงตาม url ตรงกับใน page_setting"}
    if page_setting[data['data']]["current_usage_id"] == None:
        page_setting[data['data']]["current_usage_id"] = request.sid
