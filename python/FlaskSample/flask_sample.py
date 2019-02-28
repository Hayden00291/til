from flask import Flask, render_template
import pymysql


app = Flask(__name__)


@app.route('/')
def hello():

    db = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        db='testdb',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor,
    )
    cur = db.cursor()
    sql = "select * from menbers"
    cur.execute(sql)
    members = cur.fetchall()

    cur.close()
    db.close
    name = "Hello World"
    return render_template('hello.html', title='flask test', mambers=members)


if __name__ == "__main__":
    app.run(debug=True)
