# Imports go at the top
from microbit import *
num = 0

# Code in a 'while True:' loop repeats forever
while True:
    if button_a.get_presses():
        num = num + 1
    elif button_b.get_presses():
        num = num - 1
    else:
        display.show(num)
