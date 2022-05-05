######################
#Groupe 5 TDBI2
#BAISS Salma 
#RODRIGUEZ Diana
#SALIC Awena
#https://github.com/uvsq22101985/projetIN200N
######################

import tkinter as tk

WIDTH = 350
HEIGHT = 350
largeur_case = WIDTH // 5
hauteur_case = HEIGHT // 7
color = "#18534F"


###########################
###FONCTIONS###
###########################

def souris(event):
    global color
    posx = event.x
    posy = event.y
    
    color = "yellow"
    clic_rec = canvas.find_closest(posx, posy)
    canvas.itemconfig(clic_rec, fill = color)

#############################
# Programme Principal #
racine = tk.Tk()
racine.title("Puissance 4")

canvas = tk.Canvas(racine, width=WIDTH, height= HEIGHT, bg = '#226D68')
canvas.bind('<Button-1>', souris)

# Creation grille de jeu

for i in range(5):
    for j in range(7):
        rectangle = canvas.create_rectangle((i*largeur_case, j*hauteur_case),
                ((i+1)*largeur_case, (j+1)*hauteur_case), fill=color)
        
# Boutons

bouton_save = tk.Button(racine, text="Sauvegarder")
bouton_annuler = tk.Button(racine, text="Annuler")
bouton_icone1 = tk.Button(racine, text = "Joueur 1")
bouton_icone2 = tk.Button(racine, text = "Joueur 2" )

# Placements des widgets
bouton_save.grid(row =8, column = 1)
bouton_annuler.grid(row = 8, column = 5)
bouton_icone1.grid(row = 0, column = 1)
bouton_icone2.grid(row = 0, column = 5)
canvas.grid(row=1, column=1, columnspan=5)


racine.mainloop()