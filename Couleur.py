#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random

aTrouver=[]
Trouver=[]

def Random_Couleur(f):
    """
    On renvoie un tableau de f caractère selon la difficulté, ce sont les couleurs à trouver
    """
    couleur = ['bleu','rouge','vert','jaune']
    for i in range (f):
        choix = random.choice(couleur)
        aTrouver.append(choix)
    return aTrouver

def Bonne_Couleur(couleur_aleatoire,couleur_clique):
    """
    On compare le tuple contenant le centre du clique avec le tuple contenant le centre de la bonne couleur
    """
    if couleur_clique==couleur_aleatoire:
       return True
    else:
       return False

def Appartient_Couleur(x_clique,y_clique):
    """
    Selon l'endroit du clique on dit sur quelle couleur on a cliqué
    """
    if 110<=x_clique and x_clique<=310 and 30<=y_clique and y_clique<=230:
        return "vert"
    elif 110<=x_clique and x_clique<=310 and 250<=y_clique and y_clique<=450:
        return"rouge"
    elif 330<=x_clique and x_clique<=530 and 30<=y_clique and y_clique<=230:
        return "jaune"
    elif 330<=x_clique and x_clique<=530 and 250<=y_clique and y_clique<=450:
        return "bleu"
