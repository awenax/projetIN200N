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
grille = [[0] * 7 for i in range(6)]   # le tableau fait 7 colonnes de 6 lignes
grille_save = grille
gagne = False
lst = []

#############################
# Fonctions
def get_button(b):
    global gagne
    global lst
    
    if gagne:
        return
    x = b-1
    y = playable_grid(player_colour, x, grille)
    # pas la peine de tester les alignements si il y a moins de 7 jetons dans la grille
    if len(lst) < 7:
        return
    nb_jetons = 0
    # test alignement vertical
    if (y < 3):                 # pas la peine de tester en vertical si il y a moins de 4 jetons dans la colonne
        for i in range (5):
           if grille [i][x] == grille [i+1][x] and grille [i][x] != 0:
                nb_jetons += 1
                if nb_jetons == 3:             # 3 parce que 3 comparaisons suffisent
                    print ("gagné vertical")
                    gagne = True
                    print ("Partie terminée : le vainqueur est ", player_turn )
                    return
           else:
             nb_jetons = 0
 
    nb_jetons = 0
    # test alignement horizontal
    for i in range (5):
         if grille [y][i] == grille [y][i+1] and grille [y][i] != 0:
            nb_jetons += 1
            if nb_jetons == 3:              # 3 parce que 3 comparaisons suffisent
                print ("gagné horizontal")
                gagne = True
                print ("Partie terminée : le vainqueur est ", player_turn )
                return
         else:
            nb_jetons = 0

    print ("toto")
    #
    # test alignement diagonal
    print("test alignement diagonal")
    for i in range(x-3,x+3):
        if i >= 0 and i < 6:
            for j in range (y-3, y+3):
                if j >= 0 and j < 5:
                    if grille [j][i] == grille [j+1][i+1] and grille [y][i] != 0 and grille [j+1][i+1] != 0:
                        nb_jetons += 1
                    else:
                        nb_jetons = 0
                    if nb_jetons == 3:              # 3 parce que 3 comparaisons suffisent
                        print ("gagné diagonal")
                        gagne = True
                        print ("Partie terminée : le vainqueur est ", player_turn )
                        return



def set_grid(grille):
    """Fonction qui remets la grille à 0"""
    x, y = 0, 0
    while(grille[y][x]): 
        X = 0
        while(grille[y][x]):
            grille[y][x] = 0
            X += 1
        y +=1
    return(grille)

def annuler_coup():
    """Fonction qui permets de revenir un coup en arriere"""


def load():
    """Fonction qui permets de charger une partie déjà sauvegardée"""


def save():
    """Fonction qui permet de sauvegarder une partie en cours"""


def new_game():
    """Fonction qui permet de démarrer une nouvelle partie """
    # la fonction set_grille au dessus peut aider pour remetter la grille à zéro, 
    # elle n'est pas fonctionnelle mais peut etre utile


def playable_grid(player_colour, X, grille):
    """Fonction qui va lancer le jeu et verifier, ligne par ligne,
    dans la colonne choisie par le joueur
    s'il y a ou non des obstacles"""
    global lst
    y = 5
    while(grille[y][X] != 0):
        y -=1
    if y == -1:
        not changement_joueur()
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
        changement_joueur()
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
    bouton_roll.destroy()
    

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
bouton_annuler = ttk.Button(racine, text = "Retour", command=lambda:annuler_coup)
bouton_save = ttk.Button(racine, text="Sauvegarder", command=lambda: save)
bouton_load = ttk.Button(racine, text="Charger", command=lambda:load)
bouton_newgame = ttk.Button(racine, text = "Nouvelle partie", command=lambda: new_game)
bouton_roll = ttk.Button(racine, text = "Roll", command = beginner_player)
bouton_column1 = ttk.Button(racine, text = "1", command=lambda:get_button(1))
bouton_column2 = ttk.Button(racine, text = "2", command=lambda:get_button(2))
bouton_column3 = ttk.Button(racine, text = "3", command=lambda:get_button(3))
bouton_column4 = ttk.Button(racine, text = "4", command=lambda:get_button(4))
bouton_column5 = ttk.Button(racine, text = "5", command=lambda:get_button(5))
bouton_column6 = ttk.Button(racine, text = "6", command=lambda:get_button(6))
bouton_column7 = ttk.Button(racine, text = "7", command=lambda:get_button(7))


# Placements des widgets/boutons
bouton_annuler.grid(row = 8, column = 1, columnspan=1)
bouton_save.grid(row =8, column = 7, columnspan= 1)
bouton_load.grid(row = 8, column = 6, columnspan= 1)
bouton_newgame.grid(row = 8, column = 2, columnspan=1)
bouton_roll.grid(row = 8, column = 4, columnspan= 1)
bouton_column1.grid(row = 0, column = 1)
bouton_column2.grid(row = 0, column = 2)
bouton_column3.grid(row = 0, column = 3)
bouton_column4.grid(row = 0, column = 4)
bouton_column5.grid(row = 0, column = 5)
bouton_column6.grid(row = 0, column = 6)
bouton_column7.grid(row = 0, column = 7)

canvas.grid(row=1, column=1, columnspan=7)

racine.mainloop()