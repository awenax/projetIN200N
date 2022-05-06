######################
#Groupe 5 TDBI2
#BAISS Salma 
#RODRIGUEZ Diana
#SALIC Awena
#https://github.com/uvsq22101985/projetIN200N
######################
# Variables

from re import X
import tkinter as tk
from tkinter.tix import COLUMN

WIDTH = 560
HEIGHT = 560
largeur_case = WIDTH // 7
hauteur_case = HEIGHT // 6
color = "#18534F"

#############################
# Fonctions

def souris(event):
    global color
    global X
    posx = event.x
    posy = event.y
    
    color = "yellow"
    X = COLUMN(posx)
    

#############################
# Programme Principal #

racine = tk.Tk()
racine.title("Puissance 4")

canvas = tk.Canvas(racine, width=WIDTH, height= HEIGHT, bg = '#226D68')
canvas.bind('<Button-1>', souris)

# Création de la grille
for i in range(7):
    for j in range(6):
        rectangle = canvas.create_rectangle((i*largeur_case, j*hauteur_case),
                ((i+1)*largeur_case, (j+1)*hauteur_case), fill=color)