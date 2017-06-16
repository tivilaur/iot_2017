import RPi.GPIO as GPIO
import time

P = 22 #Autoilijoiden punainen valo
K = 5  #Autoilijoiden keltainen valo
V = 6  #Autoilijoiden vihreä valo

NAPPI = 26 #Painike

P2 = 19 #Kävelijöiden punainen valo
V2 = 13 #Kävelijöiden vihreä valo

GPIO.setmode(GPIO.BCM)
GPIO.setup(P, GPIO.OUT) 
GPIO.setup(K, GPIO.OUT) 
GPIO.setup(V, GPIO.OUT)
GPIO.setup(V2, GPIO.OUT)
GPIO.setup(P2, GPIO.OUT)

GPIO.setup(NAPPI, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Painike ylhäällä

while True: #Kuunnellaan painiketta

            
    GPIO.output(V, True)  #Autoilijoille vihreä 
    GPIO.output(P2, True) #Jalankulkijoille punainen
    
    painettu = GPIO.input(26) 
    if painettu == False: #Painike painettu alas

        GPIO.output(V, False) #KAutoilijoiden vihreä poistuu
        GPIO.output(P2, False)#Kävelijöiden punainen poistuu
        GPIO.output(P, True)  #Autoilijoille punainen
        GPIO.output(V2, True) # Kävelijöille vihreä
        time.sleep(2)

        GPIO.output(V2, False)#Kävelijöiden vihreä päättyy
        GPIO.output(P, False) #Autoilijoiden punainen päättyy

GPIO.cleanup ()


