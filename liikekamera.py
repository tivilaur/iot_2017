## Liikkeentunnistava kamera

import RPi.GPIO as GPIO
import time
from picamera import PiCamera

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.IN)

camera = PiCamera()

##Tarkastellaan ympäristöä 20s ajan
loppu = time.time() + 20
while time.time() < loppu:

    
    i=GPIO.input(22)
    if i==0:
        time.sleep(0.1)
    elif i==1:
        camera.capture('liikekuva.jpg')
        time.sleep(0.1)

GPIO.cleanup()
