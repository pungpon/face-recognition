from flask import render_template, request, url_for,redirect

from app.main import main
from app.util import set_only_one_tabs

# หน้าหลัก หรือหน้าแรก path="/" (index) 
@main.route('/')
def index():
    # เช็ค ว่าใช้ 1tab/server
    if set_only_one_tabs("index"):
        # ถ้ามีการใช้งานอยู่ เปลี่ยนไปหน้า error
        return redirect(url_for("main.error"))
    # render index.html
    return render_template("index.html")

# หน้า error path="/error" 
@main.route('/error')
def error():
    # render errors/only_one_tab.html
    return render_template("errors/only_one_tab.html")

