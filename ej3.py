# Imports go at the top
from microbit import *
import music
Notas = ['a:4','g']
Notas2 = ['a3','g2']
while True:
    if button_a.is_pressed():
        music.play(Notas)
        display.show(Image.ANGRY)
        sleep(400)
    elif button_b.is_pressed():
        music.play(Notas2)
        display.show(Image.CHESSBOARD)
        sleep(400)
        
