import tkinter as tk
from random import randint

L = ["blue","blue, green, black, yellow, magenta, red."]
def cercle(n="blue"):
    x = randint(70,500)
    y = randint(70,500)
    cercle = canvas.create_oval((x,y),(x+100,y+100),fill=n)
    print(cercle)

dessin = tk.Tk()
dessin.title("Ma cible")
canvas = tk.Canvas(dessin, bg="black", height=600 , width=600, borderwidth=50 )
canvas.grid(row=1, column=1,rowspan=10)