from flask import Flask, render_template
import sqlite3


app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    conn = sqlite3.connect('./data/test.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    info = c.execute("select * from info")
    infos = info.fetchall()
    return render_template('index.html', infos=infos)


if __name__ == '__main__':
    app.run()
