import tkinter as tk
from random import randint

L = ["blue", "green", "black", "yellow", "magenta", "red"]


cible = tk.Tk()
cible.title("Ma cible")
canvas = tk.Canvas(cible, bg="black", height=600 , width=600, borderwidth=0 )
canvas.grid(row=0, column=0)
n=0
for i in range (5):
    for j in range (6):
        cercle = canvas.create_oval((0+n*10,0+n*10),(600-n*10,600-n*10),fill=L[j])
        n += 1
       
        


cible.mainloop()