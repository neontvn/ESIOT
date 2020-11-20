import Adafruit_DHT
while True:
    hum, temp = Adafruit_DHT.read_retry(11, 4)
    print "Temperature: ", temp
    print "Humidity: ", hum