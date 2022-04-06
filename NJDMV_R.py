import requests
import re
import time
from bs4 import BeautifulSoup
from datetime import datetime

import os, sys

location_arr = ['209','210','211','212','213','214','215','216','217','218','219','220','221','222','223','224','225','226','227','228','229','230']
locationname_arr = ['Lawrenceville','Bayonne','North Cape May','Camden','Cardiff','Salem','Delanco','Eatontown','SouthPlainfield','Edison','Flemington','Toms River','Freehold','Lodi','Vineland','Newark','North Bergen','Wayne','Oakland','Paterson','Thorofare','Rahway','Randolph']
base_url_link='https://telegov.njportal.com/njmvc/AppointmentWizard/11'   #  stateid
#required_months = ['April']
#required_months = ['April','May']
required_months = ['October','November']

def beep():
    os.system('omxplayer beep-01a.wav')


def job():
    print("\nChecking appointments")
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("\nDate Time: ", dt_string, "\n")
    i=0
    found=0
    
    for location in location_arr:
        print(location)
        page_html = requests.get(base_url_link+location)

        soup = BeautifulSoup(page_html.text ,'lxml')
        unavailable=soup.find('div',attrs={'class': 'alert-danger'})
        if unavailable is not None :
            print('No appointments are available in '+locationname_arr[i])
            dt_string=""
        else:
            dates_html = soup.find('div',attrs={'class': 'col-md-8'})
            date_string = dates_html.find('label',attrs={'class': 'control-label'})
            if set(required_months) & set(date_string.text.split()):
                print("Matching required months")
                date_string=re.sub('Time of Appointment for ', '', date_string.text)
                date_string=re.sub(':', '', date_string)
                message = 'DL Renew Dates: '+locationname_arr[i]+' / ('+location+') : '+date_string
                print(message)
                beep()
                found=1
        i=i+1
        
while True :
    try:
        job()
    except:
        print("Something went wrong")
        time.sleep(60)
    else:
        time.sleep(60)
