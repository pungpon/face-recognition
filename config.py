import os
#ดึง root path
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # กำหนดค่า SECRET_KEY
    SECRET_KEY = 'SECRET_KEY'
    # กำหนด path database
    DATABASE_URI = os.path.join(basedir, 'database/app.db')
    DATABASE_SQL = os.path.join(basedir, 'database/table.sql')
