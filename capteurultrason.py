from machine import Pin, I2C
from ssd1306 import SSD1306_I2C #librairie de l'ecran
import utime

WIDTH = 128 #pixels
HEIGHT = 64

i2c = I2C(0, scl = Pin(17), sda = Pin(16), freq=400000) # port d'entrée et sortie de l'ecran
display = SSD1306_I2C(WIDTH, HEIGHT, i2c) # initilisation de l'affichage de l'ecran


trigger = Pin(21, Pin.OUT) #emplacment du composant ultrason ( envoie signal)
echo = Pin(20, Pin.IN) #emplacment recupération du signal 


def ultra(): #fonction pour le composant ultrason pour l'envoie du signal 
   trigger.low() 
   utime.sleep_us(2)#temps en microsecondes pendant lequel le composant envoie un signal très faible
   trigger.high()
   utime.sleep_us(5)#temps en microsecondes pendant lequel le composant envoie un signal très fort 
   trigger.low()
   while echo.value() == 0: #boucle pour composant ultrason lorsqu'il ne percoit pas de signal
       signaloff = utime.ticks_us() # temps enregistré pendant lequel on ne recoit aucun signal
       
   while echo.value() == 1: #boucle reception d'un signal
       signalon = utime.ticks_us() # temps noté dès reception d'un signal et ensuite calcule de la distance
       
   timepassed = signalon - signaloff #calcul du temps  et apres ligne du dessous de la distance en fonction du temps distance = vitesse x temps
   distance = (timepassed * 0.0343) / 2 # distance = temps entre envoie et réception du signal x vitesse ultrason(0.0343 constante) /2 (avec convertion en cm)
   distance = "{:.1f}".format(distance) # utilisation de la fonction .format pour l'affichage de la distance avec une seule décimale
   
   print(distance + " cm")#afficher la distance dans la console
   
   return str(distance)


while True: #boucle pour afficher la distance sur l'ecran 
    display.text(ultra(),0,0) #afficher le texte de la fonction ultra
    display.show()
    display.fill(0)
    utime.sleep(1) #afficher la distance pendant 1 seconde ou se mettre à jour toutes les secondes
    

    
    