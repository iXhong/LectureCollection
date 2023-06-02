from flask import Flask, render_template
import csv
from datetime import datetime
# from apscheduler.schedulers.background import BackgroundScheduler
# from waitress import serve


app = Flask(__name__)


# def job():
#     """
#     定时任务，每次执行调用save.py进行数据爬取以及更新存储
#     :return:
#     """
#     path = './data/data.csv'
#     save.csv_save(path)
#     print(f"job {datetime.now()} ok")
#
#
# scheduler = BackgroundScheduler(daemon=True)
# scheduler.add_job(job, 'interval', hours=6)
# scheduler.start()
# # set up the schedule job


@app.route('/')
def index():  # put application's code here
    csvfile = open('./data/data.csv', newline='')
    infos = csv.DictReader(csvfile, delimiter=',')
    return render_template('index.html', infos=infos)


if __name__ == '__main__':
    # serve(app, host='0.0.0.0', port=5000)
    app.run()

