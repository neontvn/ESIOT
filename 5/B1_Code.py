import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(16, GPIO.IN)
while True:
    i = GPIO.input(16)
    if i==1:
        GPIO.output(18, False)
        print("No obstacle")
        time.sleep(0.1)
    elif i==0:
        GPIO.output(18, True)
        print("Obstacle found")
        time.sleep(0.1)