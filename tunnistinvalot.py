import RPi.GPIO as GPIO
import time

P = 22 #Autoilijoiden punainen valo
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

GPIO.setup(17, GPIO.IN)
GPIO.setup(NAPPI, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Painike ylhäällä

while True: #Kuunnellaan painiketta

    GPIO.output(V, True)  #Autoilijoille vihreä
    GPIO.output(P2, True) #Kävelijöille punainen
    GPIO.output(V2, False)#Kävelijöiden vihreä päättyy
    GPIO.output(P, False) #Autoilijoiden punainen päättyy
    
    painettu = GPIO.input(26) 
    if painettu == False: #Painike painettu alas

        loppu = time.time() + 20
        while time.time() < loppu: ##Tarkastellaan liikennettä 20s ajan
            
        
            i=GPIO.input(17) ##sensori
            if i==0:         ##Liikettä ei havaita

                print ("Ei havaita liikettä")
                GPIO.output(V, False) #Autoilijoiden vihreä päättyy
                GPIO.output(P, True)  #Autoilijoille punainen
                GPIO.output(P2, False)#Kävelijöiden punainen poistuu
                GPIO.output(V2, True) # Kävelijöille vihreä
                time.sleep(0.1)


            elif i==1: ##Liikettä havaitaan

                print ("Liikettä havaittu")

                GPIO.output(P, False) #Autoilijoiden punainen päättyy
                GPIO.output(V, True)  #Autoilijoille vihreä
                GPIO.output(V2, False)#Kävelijöiden vihreä päättyy
                GPIO.output(P2, True) #Kävelijöille punainen
                time.sleep(0.1)
                
GPIO.cleanup ()

