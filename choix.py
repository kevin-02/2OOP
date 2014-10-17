#!/usr/bin/python

import random

aTrouver=[]

def couleur(f):
    couleur = ['bleu','rouge','vert','jaune']
    for i in range (f):
        choix = random.choice(couleur)
        aTrouver.append(choix)
    return aTrouver
