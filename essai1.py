######################
#Groupe 5 TDBI2
#BAISS Salma 
#RODRIGUEZ Diana
#SALIC Awena
#https://github.com/uvsq22101985/projetIN200N
######################

import tkinter as tk
from turtle import width

WIDTH = 800
HEIGHT = 600

###########################
###FONCTIONS###
###########################




###########################
racine = tk.Tk()
racine.title("Puissance 4")

canvas = tk.Canvas(racine, width=WIDTH, height= HEIGHT, bg = '#226D68')


bouton_save = tk.Button(racine, text="Sauvegarder")
bouton_annuler = tk.Button(racine, text="Annuler")
bouton_icone1 = tk.Button(racine, text = "Joueur 1")
bouton_icone2 = tk.Button(racine, text = "Joueur 2" )

#placements des widgets
bouton_save.grid(row =8, column = 1)
bouton_annuler.grid(row = 8, column = 5)
bouton_icone1.grid(row = 0, column = 1)
bouton_icone2.grid(row = 0, column = 5)
canvas.grid(row=1, column=1, columnspan=5)


racine.mainloop()