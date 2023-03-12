import requests
import os
import datetime
from time import sleep

ip_rest_api = os.environ.get('REST_API_IP')
url = "http://"+ip_rest_api +"/api/cleanoldlogs/"
headers = {"Content-Type": "application/json; charset=utf-8"}
  

sleep(15)
print(url)
print("Program started...")
while True:

    temp_time = datetime.datetime.now()
    if(temp_time.hour==19 and temp_time.minute==22 and temp_time.day==1):
        error = ""
        try:
            r1 = requests.get(
                url+"1",
                headers=headers
            )
        except Exception as e:
            error = e
        temp_time_str = temp_time.strftime("%m/%d/%Y, %H:%M:%S")
        if error=="":
            print(f"Done {temp_time_str} {r1.json()}")
        else:
            print(f"Error {temp_time_str} {error}")
    sleep(60)
