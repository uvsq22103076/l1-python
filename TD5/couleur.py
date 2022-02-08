import tkinter as tk
from random import randint

def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)
print(get_color(200, 200, 200))

def draw_pixel(i,j,color):
    pix = canvas.create_line((i,j),(i+1,j+1),fill=color)
print(draw_pixel(256/2,256/2,"white"))


couleur = tk.Tk()
couleur.title("Couleur")
canvas = tk.Canvas(couleur, bg="black", height=256 , width=256, borderwidth=0 )
canvas.grid(row=0, column=1, rowspan=6)

button = tk.Button(couleur, text="Aléatoire", fg="blue" , bg="light grey", padx=0, pady=0, font = ("helvetica", "20"))
button.grid(row=0, column=0)

button1 = tk.Button(couleur, text="Dégradé gris", bg="light grey", fg="blue", padx=0, pady=0, font = ("helvetica", "20") )
button1.grid(row=2, column=0)

button2 = tk.Button(couleur, text="Dégradé 2D", bg="light grey", fg="blue", padx=0, pady=0, font = ("helvetica", "20") )
button2.grid(row=4, column=0)

couleur.mainloop()