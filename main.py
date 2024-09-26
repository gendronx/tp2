"""
Xavier Gendron
404
ce programme fait deviné un nombre aléatoire
"""

import random

intervalle = int(input("Le programme choisira un nombre entre 0 et: "))
nb = random.randint(0, intervalle)
print(f"J'ai choisi un nombre entre 0 et {intervalle}, à vous de le deviner \nBonne chance")

nbessai = 0


def nbmystere(nb_essai):
    essai = int(input("Entrez un nombre: "))

    if essai > nb:
        print("Le nombre que vous avez entrer est trop grand")
        nb_essai += 1
        nbmystere(nb_essai)

    elif essai < nb:
        print("Le nombre que vous avez entrer est trop petit")
        nb_essai += 1
        nbmystere(nb_essai)

    elif essai == nb:
        print("Bravo, vous avez trouver le nombre secret")
        nb_essai += 1
        print("Vous avez réussi en", nb_essai, "essai")
        newgame = input("Voulez-vous faire une autre parti y/n: ")

        if newgame == "y":
            nb_essai = 0
            nbmystere(nb_essai)

        elif newgame == "n":
            print("Merci d'avoir joué")

        else:
            print("Cette réponse na pas pu être accepté")


nbmystere(nbessai)
