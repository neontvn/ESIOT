import RPi.GPIO as GPIO
from subprocess import call
import time
import os
import glob
import smtplib
import base64
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import subprocess
gmail_user = "​ checking999mail@gmail.com​ "
gmail_pwd = "mail999checking"
FROM = '​ checking999mail@gmail.com​ '
TO = ['hyd.embedded@pantechmail.com'] #must be a list
i=1
while (i):
    i=i-1
    subprocess.Popen( "fswebcam -r 1280x720 /home/pi/Downloads/pan.jpg", shell=True )
    time.sleep(1)
    msg = MIMEMultipart()
    time.sleep(1)
    msg['Subject'] ="testing msg send from python"
    time.sleep(1)
    fp = open("/home/pi/Downloads/pan.jpg", 'rb')
    time.sleep(1)
    img = MIMEImage(fp.read())
    time.sleep(1)
    fp.close()
    time.sleep(1)
    msg.attach(img)
    time.sleep(1)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
        print "smtp.gmail"
        server.ehlo()
        print "ehlo"
        server.starttls()
        print "starttls"
        server.login(gmail_user, gmail_pwd)
        print "reading mail & password"
        server.sendmail(FROM, TO, msg.as_string())
        print "from"
        server.close()
        print 'successfully sent the mail'
    except:
        print "failed to send mail"