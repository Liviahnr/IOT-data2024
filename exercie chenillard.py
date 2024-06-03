import utime

print("ok")
utime.sleep(1)
print("delay de 1")
from machine import Pin # importe dans le code la lib qui permet de gerer les Pins de sortie
import utime # importe dans le code la lib qui permet de gerer le temps

pinNumber = 17 # declaration d'une variable pinNumber à 17 pour la premiere led 
pinNumber2 = 14 # idem deuxieme led
pinNumber3 = 10 # idem troisieme led

led = Pin(pinNumber, mode=Pin.OUT)# declaration d'une variable de type pin 17 #et on prescise que c'est une pin de sortie de courant (OUT)
led2 = Pin(pinNumber2, mode=Pin.OUT)
led3 = Pin(pinNumber3, mode=Pin.OUT)

while True:          # boucle infini
    led.toggle()     # change l'etat de la led
    utime.sleep(0.2) # le temps que la première led s'allume
    led2.toggle()
    utime.sleep(0.3) # temps d'attente deuxieme led
    led3.toggle()
    utime.sleep(0.2) # temps d'attente troisieme led 
    # attendre 1 seconde 
  