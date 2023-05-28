import csv

from flask import Flask, render_template
import sqlite3


app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    csvfile = open('./data/test.csv', newline='')
    infos = csv.DictReader(csvfile)

    return render_template('index.html', infos=infos)


if __name__ == '__main__':
    app.run()
