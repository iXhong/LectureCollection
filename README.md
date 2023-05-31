# Lecture Collection
***
A web application used to collect information of academic lectures from a few college websites.

*This is my first Flask project,if you find anything wrong or needed to be improved,Don't hesitate, and contact me!!*

## Usage
***
### Docker
I recommend you to use Docker to run this app, git clone the source code and
build it, then just run:
```shell
docker run -p 5000:5000 -d lecturecollection:latest
```
check the localhost:5000 , you will find it.

### Python
If you wish to run this app with python, 
```shell
git clone git@github.com:iXhong/LectureCollection.git
cd LectureCollection
pip install -r requirements.txt
python3 app.py
```
It should work.

## Details
***
+ ### Work principle
  + web_info.py: get information from websites 
  + save.py: use web_info.py to get information of all the websites in college.json and save them in the /data/data.csv
  + app.py: cron job setting and run the application

## Contributing
***
PRs accepted.