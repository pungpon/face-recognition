import sqlite3
#ดึง คลาส Config
from config import Config

# สร้าง Class Database สืบทอดจาก Class Config
class Database(Config):
    # เมื่อเรียกใช้ ให้ไปเชื่อมกับ database ที่กำหนด ใน Config.DATABASE_URI
    def __init__(self):
        self.db = sqlite3.connect(Config.DATABASE_URI, check_same_thread=False)
    def connect(self):
        return self.db
    def init(self):
        # เปิดไฟล์ จาก database ที่กำหนด ใน Config.DATABASE_SQL
        with open(Config.DATABASE_SQL, 'r') as sql_file:
            # กำหนด ตัวแปล ให้เป็น สตริงจากไฟล์
            sql_script = sql_file.read()
        # คิวรี่ ข้อมูลจาก sql_script
        self.db.cursor().executescript(sql_script)
        # บันทึกลงฐานข้อมูล
        self.db.commit()
        # ปิดการเชื่อมต่อ
        self.db.close()