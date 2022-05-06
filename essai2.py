######################
#Groupe 5 TDBI2
#BAISS Salma 
#RODRIGUEZ Diana
#SALIC Awena
#https://github.com/uvsq22101985/projetIN200N
######################

# Variables
import tkinter as tk
from tkinter import ttk
import random

WIDTH = 560
HEIGHT = 560
largeur_case = WIDTH // 7
hauteur_case = HEIGHT // 6
color = "#18534F"
player_1 = 1
player_2 = 2
grille = [[0] * 6 for i in range(7)]
y = 0

#############################
# Fonctions
def get_button(b):
    global X
    X = b-1
    print(X)

def set_grid(grille):
    global X, y
    """Fonction qui remets la grille à 0"""
    X, y = 0, 0
    while(grille[y][X]): 
        X = 0
        while(grille[y][X]):
            grille[y][X] == 0
            X += 1
        y +=1
    return(grille)

def playable_grid(player_colour, X, grille):
    global y
    """Fonction qui va lancer le jeu et verifier 
    dans la colonne choisie par le joueur
    s'il n'y a pas d'obstacle"""
    y = 5
    while(grille[y][X] != 0):
        y -=1
    if(grille[y][X] == 0):
        grille[y][X] = player_colour
    return y

def player_begin():
    global player_1, player_2
    
    


#############################
# Programme Principal #

racine = tk.Tk()
racine.title("Puissance 4")

canvas = tk.Canvas(racine, width=WIDTH, height= HEIGHT, bg = '#226D68')

# Création de la grille
for i in range(7):
    for j in range(6):
        rectangle = canvas.create_rectangle((i*largeur_case, j*hauteur_case),
                ((i+1)*largeur_case, (j+1)*hauteur_case), fill=color)

# Boutons
bouton_setgrid = ttk.Button(racine, text = "Rejouer", command=set_grid(grille))
bouton_column1 = ttk.Button(racine, text = "1", command=lambda:get_button(1))
bouton_column2 = ttk.Button(racine, text = "2", command=lambda:get_button(2))
bouton_column3 = ttk.Button(racine, text = "3", command=lambda:get_button(3))
bouton_column4 = ttk.Button(racine, text = "4", command=lambda:get_button(4))
bouton_column5 = ttk.Button(racine, text = "5", command=lambda:get_button(5))
bouton_column6 = ttk.Button(racine, text = "6", command=lambda:get_button(6))
bouton_column7 = ttk.Button(racine, text = "7", command=lambda:get_button(7))


# Placements des widgets/boutons
bouton_setgrid.grid(row = 8, column = 1, columnspan=1)
bouton_column1.grid(row = 0, column = 1)
bouton_column2.grid(row = 0, column = 2)
bouton_column3.grid(row = 0, column = 3)
bouton_column4.grid(row = 0, column = 4)
bouton_column5.grid(row = 0, column = 5)
bouton_column6.grid(row = 0, column = 6)
bouton_column7.grid(row = 0, column = 7)
canvas.grid(row=1, column=1, columnspan=7)
racine.mainloop()