from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

keyboard = KeyboardController()
mouse = MouseController()

print ("Current position: " + str(mouse.position)) #Récupérer position de la souris (-1920,0 => 3840,1080)
mouse.position = (960,540) #Positionnement de la souris
mouse.click(Button.left, 1) #Click souris (left,right,middle) et nombre
mouse.press(Button.left) #Maitien du click
mouse.release(Button.left) #Relache du click
