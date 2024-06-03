import network   #import des fonction lier au wifi
import urequests	#import des fonction lier au requetes http
import utime	#import des fonction lier au temps
import ujson	#import des fonction lier à la convertion en Json
from machine import Pin, PWM # importe dans le code la lib qui permet de gerer les Pin de sortie et de modulation du signal
import utime
import random

rouge = PWM(Pin(17,mode=Pin.OUT)) # emplacement pin Led rouge

rouge.freq(1_000) # dont la frequence est de 1000 (default)
rouge.duty_u16(0000) # faire changer l'intensité 

vert = PWM(Pin(18,mode=Pin.OUT))# emplacement pin Led verte

vert.freq(1_000) # dont la frequence est de 1000 (default)
vert.duty_u16(0000)

bleu = PWM(Pin(19,mode=Pin.OUT))# emplacement Led pin rouge

bleu.freq(1_000) # dont la frequence est de 1000 (default)
bleu.duty_u16(0000)

wlan = network.WLAN(network.STA_IF) # met la raspi en mode client wifi
wlan.active(True) # active le mode client wifi

ssid = 'Pixel_7deLivia'
password = 'Marionchou'
wlan.connect(ssid, password) # connecte la raspi au réseau
url = "https://hp-api.lainocs.fr/characters"



colors = {"Gryffindor":(30000,000,000), #rouge
          "Slytherin":(1000, 30000, 1000), # vert
          "Hufflepuff":(int((22730000)/255), 20000, 1000),#jaune/orange
          "Ravenclaw":(int((3030000)/255), int((144*30000)/255), 30000), #bleu
          "":(30000, 30000, 30000)}#couleur par default (blanc)
 
while not wlan.isconnected():
    print("pas co")
    utime.sleep(1)
    pass

while(True):
    try:
        print("GET")
        r = urequests.get(url) # lance une requete sur l'url
        rd = random.randint(1,30) #creation d'une function pour obtenir un chiffre aléatoire
        name = r.json()[rd]["name"] # on récupère le chiffre aléatoire obtenu pour chosir un personnage aléatoire
        house = r.json()[rd]["house"] #on récupère dans le tableau la valeur du nom et de la maison du personnage
        #print(r.json()) # traite sa reponse en Json
        print(name) #affiche le personnage avec sa maison 
        print(house)
        
        rouge.duty_u16(colors[house][0]) # Allumer la LED RGB avec la couleur correspondante à la maison sélectionné
        vert.duty_u16(colors[house][1])
        bleu.duty_u16(colors[house][2])
         # Utilisation de la couleur par défaut si la maison n'est pas dans le dictionnaire
        utime.sleep (1)
    
        r.close() # ferme la demande
        utime.sleep(1)
    
        
    except Exception as e:
        print(e)
    

    
    
