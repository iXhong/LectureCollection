# *Lecture Collection*
A web application used to collect information on academic lectures from a few college website

***
*This is my first Flask project,if you find anything wrong or needed to be improved,*Don't hesitate, and contact me!!*
## Usage
I recommend you to use Docker to run this app.
```shell
docker run -p 5000:5000 lecturecollection:latest
```
check the localhost:5000 , you will find it.

## Details
+ ### Work principle
  + web_info.py: get information from websites 
  + save.py: use web_info.py to get information of all the websites in college.json and save them in the /data/data.csv
  + app.py: cron job setting and run the application
