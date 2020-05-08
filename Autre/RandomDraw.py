from turtle import *
import time
import random

speed(0)
color("black")

tab = [up(), down(), right(90), left(90)]

for i in range (100):
    tab[random.randrange(0,4)]
    forward(10)

time.sleep(10)