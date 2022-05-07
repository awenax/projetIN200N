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

from pkg_resources import get_default_cache

WIDTH = 560
HEIGHT = 560
largeur_case = WIDTH // 7
hauteur_case = HEIGHT // 6
color = "#18534F"
player_1 = 1
player_2 = 2 
grille = [[0] * 7 for i in range(6)]                # le tableau fait 7 colonnes de 6 lignes
grille_save = grille
gagne = False
lst = []


#############################
# Fonctions
def get_button(b):
    global gagne
    
    if gagne:
        return
    X = b-1
    changement_joueur()
    y = playable_grid(player_colour, X, grille)
    nb_jetons = 0
    # test alignement vertical
    if (y < 3):                 # pas la peine de tester en vertical si il y a moins de 4 jetons dans la colonne
        for i in range (5):
           if grille [i][X] == grille [i+1][X] and grille [i][X] != 0:
                nb_jetons += 1
           else:
             nb_jetons = 0
        if nb_jetons == 3:             # 3 parce que la 1ère occurence n'est pas comptée
           print ("gagné vertical")
           gagne = True
    nb_jetons = 0
    # test alignement horizontal
    for i in range (6):
        if nb_jetons == 3:              # 3 parce que la 1ère occurence n'est pas comptée
            print ("gagné horizontal")
            gagne = True
            break
        if grille [y][i] == grille [y][i+1] and grille [y][i] != 0:
            nb_jetons += 1
        else:
            nb_jetons = 0
    
    print ("toto")
    #
    # test alignement diagonal
    print("test alignement diagonal")

    if gagne == True:
        print ("Partie terminée : le vainqueur est ", player_turn )
 
def set_grid(grille):
    """Fonction qui remets la grille à 0"""
    X, y = 0, 0
    while(grille[y][X]): 
        X = 0
        while(grille[y][X]):
            grille[y][X] = 0
            X += 1
        y +=1
    return(grille)

def playable_grid(player_colour, X, grille):
    """Fonction qui va lancer le jeu et verifier, ligne par ligne,
    dans la colonne choisie par le joueur
    s'il y a ou non des obstacles"""
    global lst
    y = 5
    
    while(grille[y][X] != 0):
        y -=1
    if (y < 0):
        return y
    if(grille[y][X] == 0):
        gauche = largeur_case * X
        droite = gauche + largeur_case
        haut = hauteur_case * y
        bas = haut + hauteur_case
        # mettre dans une variable la référence à l'objet que l'on va créeer pour pouvoir le supprimer ensuite pour le undo
        obj = canvas.create_oval(((gauche, haut),(droite, bas)) , fill=player_colour)
        grille[y][X] = player_colour
        lst.append(player_colour + "," + str(X) + "," + str(y) + "," + str(obj) )
    return y

def beginner_player():
    global player_colour, player_turn
    global beginner, choice_colour
    couleurs = ["red", "yellow"]
    choice_colour = random.choice(couleurs)
    if choice_colour == "red":
        player_turn = "Joueur 1"
        player_colour = "red"
    else:
        player_turn = "Joueur 2"
        player_colour = "yellow"
    beginner = tk.Label(racine, text = player_turn, fg = player_colour, bg = "#535953")
    beginner.grid(row=8, column = 3, columnspan=3)
    

def changement_joueur():
    global player_colour, player_turn
    global beginner
    if player_turn == "Joueur 1":
        player_turn = "Joueur 2"
        player_colour = "yellow"
    else:
        player_turn = "Joueur 1"
        player_colour = "red"
    beginner = tk.Label(racine, text = player_turn, fg = player_colour, bg = "#535953")
    beginner.grid(row=8, column = 3, columnspan=3)

        

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
bouton_setgrid = ttk.Button(racine, text = "Rejouer", command= set_grid(grille))
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

beginner_player()
racine.mainloop()