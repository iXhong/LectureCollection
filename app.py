from flask import Flask, render_template
import web_info

url = "https://cise.njtech.edu.cn/index/xsdt.htm"
strainer = 'txt'
num = 15
info_list = web_info.getinfo(url, strainer, num)

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html', info_list=info_list)


if __name__ == '__main__':
    app.run()
