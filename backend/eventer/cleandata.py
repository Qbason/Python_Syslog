import requests
import os
import datetime
from time import sleep


print("Program started...")
while True:

    temp_time = datetime.datetime.now()
    if(temp_time.hour==23 and temp_time.minute==59):
        requests.get(
            os.environ.get('REST_API_IP')+"/api/cleanoldlogs/"
        )
        temp_time_str = temp_time.strftime("%m/%d/%Y, %H:%M:%S")
        print(f"Done {temp_time_str}")
    sleep(59)