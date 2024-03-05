from flask import render_template, redirect, url_for

from app.faculty import faculty

from app.database import Database

db = Database().connect()
mycursor = db.cursor()

# หน้าหลัก หรือหน้าแรก path="/" (index) 
@faculty.route('/')
def index():
    # render index.html
    mycursor.execute("""SELECT * FROM faculty""")
    data = mycursor.fetchall()
    return render_template("faculty/index.html", data=data)

# test insert faculty
@faculty.route('/test/<string:name>')
def test_insert(name):
    # render index.html
    mycursor.execute("""
                        INSERT INTO `faculty`(`id`, `name`, `stats`) 
                        VALUES 
                        (NULL,'{}',NULL)
                        """.format(name))
    db.commit()
    return redirect(url_for('faculty.index'))