import time
import RPi.GPIO as GPIO
LC-R=22
LC-Y=24
LC-G=26
LD-R=32
LD-Y=31
LD-G=16
LA-R=15
LA-Y=13
LA-G=11
LB-R=40
LB-Y=38
LB-G=37
LA=int(input(“LA:”))
print(LA)
LB=int(input(“LB:”))
print(LB)
LC=int(input(“LC:”))
print(LC)
LD=int(input(“LD:”))
print(LD)
RUNNING = True
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(LA-R, GPIO.OUT)
GPIO.setup(LA-Y, GPIO.OUT)
GPIO.setup(LA-G, GPIO.OUT)
GPIO.setup(LB-R, GPIO.OUT)
GPIO.setup(LB-Y, GPIO.OUT)
GPIO.setup(LB-G, GPIO.OUT)
GPIO.setup(LC-R, GPIO.OUT)
GPIO.setup(LC-Y, GPIO.OUT)
GPIO.setup(LC-G, GPIO.OUT)
GPIO.setup(LD-R, GPIO.OUT)
GPIO.setup(LD-Y, GPIO.OUT)
GPIO.setup(LD-G, GPIO.OUT)
def trafficState1(red1, yellow1, green1):
    GPIO.output(LA-R, red1)
    GPIO.output(LA-Y, yellow1)
    GPIO.output(LA-G, green1)
def trafficState2(red2, yellow2, green2):
    GPIO.output(LB-R, red2)
    GPIO.output(LB-Y, yellow2)
    GPIO.output(LB-G, green2)
def trafficState3(red3, yellow3, green3):
    GPIO.output(LC-R, red3)
    GPIO.output(LC-Y, yellow3)
    GPIO.output(LC-G, green3)
def trafficState4(red4, yellow4, green4):
    GPIO.output(LD-R, red4)
    GPIO.output(LD-Y, yellow4)
    GPIO.output(LD-G, green4)
print "Traffic Light Simulation. Press CTRL + C to quit"
try:
    while RUNNING:
        print("Green Light ON for LA ")
        trafficState1(0,0,1)
        trafficState2(1,0,0)
        trafficState3(1,0,0)
        trafficState4(1,0,0)
        time.sleep(LA)
        trafficState1(0,1,0)
        trafficState2(1,0,0)
        trafficState3(1,0,0)
        trafficState4(1,0,0)
        time.sleep(5)
        print("Green Light ON for LB")
        trafficState1(1,0,0)
        trafficState2(0,0,1)
        trafficState3(1,0,0)
        trafficState4(1,0,0)
        time.sleep(LB)
        trafficState1(1,0,0)
        trafficState2(0,1,0)
        trafficState3(1,0,0)
        trafficState4(1,0,0)
        time.sleep(5)
        print("Green Light ON for LC")
        trafficState1(1,0,0)
        trafficState2(1,0,0)
        trafficState3(0,0,1)
        trafficState4(1,0,0)
        time.sleep(LC)
        trafficState1(1,0,0)
        trafficState2(1,0,0)
        trafficState3(0,1,0)
        trafficState4(1,0,0)
        time.sleep(5)
        print("Green Light ON for LD")
        trafficState1(1,0,0)
        trafficState2(1,0,0)
        trafficState3(1,0,0)
        trafficState4(0,0,1)
        time.sleep(LD)
        trafficState1(1,0,0)
        trafficState2(1,0,0)
        trafficState3(1,0,0)
        trafficState4(0,1,0)
        time.sleep(5)
except KeyboardInterrupt:
    RUNNING = False print "\Quitting"
finally:
    GPIO.cleanup()