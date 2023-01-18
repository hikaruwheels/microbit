# Imports go at the top
from microbit import *
coso1 = Image("00000:18954:71148:18954:00000")
coso2 = Image("00000:00000:18954:71148:18954")
coso3 = Image("18954:00000:00000:18954:71148")
coso4 = Image("71148:18954:00000:00000:18954")
coso5 = Image("18954:71148:18954:00000:00000")

while True:
    display.show(coso1)
    sleep (200)
    display.show(coso2)
    sleep(200)
    display.show(coso3)
    sleep(200)
    display.show(coso4)
    sleep(200)
    display.show(coso5)
    sleep(200)
