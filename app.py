from flask import Flask, render_template
import csv
from apscheduler.schedulers.background import BackgroundScheduler
import save


scheduler = BackgroundScheduler()


def job():
    """
    定时任务，每次执行调用save.py进行数据爬取以及更新存储
    :return:
    """
    path = './data/data.csv'
    save.csv_save(path)


app = Flask(__name__)

scheduler.add_job(job(), id="save", trigger='interval', hours=6)


@app.route('/')
def index():  # put application's code here
    csvfile = open('./data/test.csv', newline='')
    infos = csv.DictReader(csvfile, delimiter=',')
    return render_template('index.html', infos=infos)


if __name__ == '__main__':
    scheduler.start()
    app.run()
