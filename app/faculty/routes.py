from flask import render_template

from app.faculty import faculty

# หน้าหลัก หรือหน้าแรก path="/" (index) 
@faculty.route('/')
def index():
    # render index.html
    return render_template("faculty/index.html")
