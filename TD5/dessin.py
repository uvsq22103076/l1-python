import tkinter as tk
from random import randint


def cercle(n="blue"):
    x = randint(70,500)
    y = randint(70,500)
    cercle = canvas.create_oval((x,y),(x+100,y+100),fill=n)
    print(cercle)

def carre(n="blue"):
    x = randint(70,500)
    y = randint(70,500)
    carre = canvas.create_rectangle((x,y),(x+100,y+100),fill=n)
    print(carre)

def croix(n="blue"):
    x = randint(70,500)
    y = randint(70,500)
    carre = canvas.create_rectangle((x,y),(x+100,y+100))
    diag1 = canvas.create_line((x,y),(x+100,y+100),fill=n,width=3)
    diag2 = canvas.create_line((x,y+100),(x+100,y),fill=n,width=3)
    print(carre)
    print(diag1)
    print(diag2)

def changecouleur():
    n = input("choisit une couleur parmi : white, black, red, green, blue, cyan, yellow.")
    button1.config(command=lambda : cercle(n))
    button2.config(command=lambda : carre(n))
    button3.config(command=lambda : croix(n))

dessin = tk.Tk()
dessin.title("Mon dessin")
canvas = tk.Canvas(dessin, bg="black", height=600 , width=600, borderwidth=50 )
canvas.grid(row=1, column=1,rowspan=10)



button = tk.Button(dessin, text="Choisir une couleur", command=changecouleur, bg="light grey", padx=10, pady=10, font = ("helvetica", "15"))
button.grid(row=0, column=1)

button1 = tk.Button(dessin, text="Cercle", command=cercle, bg="light grey", padx=0, pady=0, font = ("helvetica", "15") )
button1.grid(row=3, column=0)

button2 = tk.Button(dessin, text="Carre", command=carre, bg="light grey", padx=0, pady=0, font = ("helvetica", "15") )
button2.grid(row=6, column=0)

button3 = tk.Button(dessin, text="Croix", command=croix, bg="light grey", padx=0, pady=0, font = ("helvetica", "15") )
button3.grid(row=9, column=0)

dessin.mainloop()






