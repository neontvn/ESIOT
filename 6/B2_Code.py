import RPi.GPIO as GPIO
import time
from picamera import PiCamera
from time import sleep
GPIO.setmode(GPIO.BCM)
camera = PiCamera()
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
    input_state = GPIO.input(18)
    if input_state == False:
        print('Button Pressed')
        time.sleep(0.2)
        camera.start_preview()
        sleep(5)
        camera.capture('/home/pi/Projects/aaaa/image.jpg')
        camera.stop_preview()