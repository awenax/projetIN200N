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

def souris(event):
    global color
    global clic_rec
    posx = event.x
    posy = event.y
    
    color = "yellow"
    clic_rec = canvas.find_closest(posx, posy)
    canvas.itemconfig(clic_rec, fill = color)
    #mouvement()

#def mouvement():
    #canvas.move(clic_rec, 0 , 1)
    #canvas.after(20, mouvement)

#############################
# Programme Principal #
racine = tk.Tk()
racine.title("Puissance 4")

canvas = tk.Canvas(racine, width=WIDTH, height= HEIGHT, bg = '#226D68')
canvas.bind('<Button-1>', souris)

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