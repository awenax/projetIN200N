######################
#Groupe 5 TDBI2
#BAISS Salma 
#RODRIGUEZ Diana
#SALIC Awena
#https://github.com/uvsq22101985/projetIN200N
######################

import tkinter as tk

WIDTH = 560
HEIGHT = 560
largeur_case = WIDTH // 7
hauteur_case = HEIGHT // 6
color = "#18534F"


###########################
###FONCTIONS###
###########################

#def souris(event):
    #global color
    #global clic_rec
    #posx = event.x
    #posy = event.y
    
    #color = "yellow"
    #clic_rec = canvas.find_closest(posx, posy)
    #canvas.itemconfig(clic_rec, fill = color)
    #mouvement()




#############################
# Programme Principal #
racine = tk.Tk()
racine.title("Puissance 4")

canvas = tk.Canvas(racine, width=WIDTH, height= HEIGHT, bg = '#226D68')
#canvas.bind('<Button-1>', souris)

# Creation grille de jeu

for i in range(7):
    for j in range(6):
        rectangle = canvas.create_rectangle((i*largeur_case, j*hauteur_case),
                ((i+1)*largeur_case, (j+1)*hauteur_case), fill=color)
        
# Boutons

bouton_save = tk.Button(racine, text="Save")
bouton_annuler = tk.Button(racine, text="Back")
bouton_column1 = tk.Button(racine, text = "1")
bouton_column2 = tk.Button(racine, text = "2")
bouton_column3 = tk.Button(racine, text = "3")
bouton_column4 = tk.Button(racine, text = "4")
bouton_column5 = tk.Button(racine, text = "5")
bouton_column6 = tk.Button(racine, text = "6")
bouton_column7 = tk.Button(racine, text = "7")


# Placements des widgets
bouton_save.grid(row =8, column = 1)
bouton_annuler.grid(row = 8, column = 7)
bouton_column1.grid(row = 0, column = 1)
bouton_column2.grid(row = 0, column = 2)
bouton_column3.grid(row = 0, column = 3)
bouton_column4.grid(row = 0, column = 4)
bouton_column5.grid(row = 0, column = 5)
bouton_column6.grid(row = 0, column = 6)
bouton_column7.grid(row = 0, column = 7)
canvas.grid(row=1, column=1, columnspan=7)


racine.mainloop()


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
bouton_annuler = ttk.Button(racine, text = "Retour", command=lambda:annuler_coup)
bouton_save = ttk.Button(racine, text="Sauvegarder", command=lambda: save)
bouton_load = ttk.Button(racine, text="Charger", command=lambda:load)
bouton_newgame = ttk.Button(racine, text = "Nouvelle partie", command=lambda: new_game)
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