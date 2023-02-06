# Imports go at the top
from microbit import *


lista_amigos = ["Nobita","Doraemon","Suneo"]

index = 0

while True:
    if button_a.was_pressed():
        index = index + 1
        sleep(500)
    elif button_b.was_pressed():
        index = index - 1
        sleep(500)

    if index>len(lista_amigos)-1:
        index = 1
    elif index<0:
        i = len(lista_amigos)-1
    else:
        display.show(index)
        sleep(500)
        display.show(lista_amigos[index])
        sleep(500)
        
