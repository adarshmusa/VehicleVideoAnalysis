# currently edited for hackathon - will revert back to original code soon
import json 
from urllib.request import urlopen
import smtplib
import email
from datetime import datetime

# to send a notification mail 
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('adarsh.dummy.mail@gmail.com', '-enter key here-')
def mail(text):
    subject="ALERT: Stolen Vehicle Detected"
    message='Subject: {}\n\n{}'.format(subject,text)
    server.sendmail('adarsh.dummy.mail@gmail.com','adarsh.bhartimusa2012@gmail.com',message)

url='http://ipinfo.io/json'
response=urlopen(url)
data=json.load(response)
str=""

for i in data:
    if(i=='region'):
        str=str+" "+data[i]
print(str)

# datetime object containing current date and time
now = datetime.now()
from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
print("now =", now)
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


#text="The stolen vehicle is detected to be currently in {}. We are hereby informing and alerting you to proceed with the necessary actions.\n".format(str)
text="A stolen vehicle is detected to be currently in"+str+". We are hereby informing and alerting you to proceed with the necessary actions.\n"
text=text+"\nTime and Date of detection:- "+dt_string
text=text+"\n\n(Team Dynamic Aces - HCK7086)"
mail(text)