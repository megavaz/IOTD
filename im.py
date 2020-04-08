import requests
import os
from datetime import datetime
from random import randrange
from datetime import timedelta
import time

def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days)
    random_day = randrange(int_delta)
    return start + timedelta(days=random_day)


d1 = datetime.strptime('1/1/2010', '%m/%d/%Y')
d2 = datetime.now()

rnd = random_date(d1, d2).strftime("%Y-%m-%d")
api_key = ''
url = ("https://api.nasa.gov/planetary/apod?api_key=" + api_key + "&date=" + rnd)
file_path = os.path.dirname(os.path.realpath(__file__)) + r"\image_name.jpg"
request = requests.get(url).json()
print(request)
image_url = request['hdurl']
try:
    request1 = requests.get(image_url)
except:
    print('Couldn\'t get hd version :(')
    time.sleep(2)
picture = request1.content

if os.path.isfile(file_path):
    os.remove(file_path)
with open(file_path, 'wb') as handler:
    handler.write(picture)

import ctypes
SPI_SETDESKWALLPAPER = 20 
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, file_path , 0)
