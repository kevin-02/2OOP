#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
from Couleur import *
from Initial import *
import pygame
from pygame.locals import *


pygame.init()

fenetre = pygame.display.set_mode((640, 480))
masque = pygame.image.load("image/masque2.png")

#On innitialise la fenetre
initialisation(fenetre)

difficulte = 1
if difficulte == 1:
    nb = 4
    pause = 2

#On entoure la couleur choisi par Ramdom_Couleur d'un masque gris
tableau_couleur = Random_Couleur(nb)
for i in tableau_couleur:
    if i == 'vert':
        fenetre.blit(masque,(110,30))
    elif i =='jaune':
        fenetre.blit(masque,(330,30))
    elif i == 'rouge':
        fenetre.blit(masque,(110,250))
    else:
        fenetre.blit(masque,(330,250))
    pygame.display.flip()
    time.sleep(pause)
    initialisation(fenetre)
    time.sleep(0.5)

continuer = 1
clic = -1

while continuer:
    #On attend des evenements
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
        #Si on clique avec la souris...
        if event.type == MOUSEBUTTONUP and event.button == 1:
            clic = clic + 1
            if clic == 4:
                break
            try:
                #On veut savoir à qu'elle couleur appartient l'nedroit du clique
                couleur = Appartient_Couleur(event.pos[0],event.pos[1])
                #On regarde si la couleur est la même
                if Bonne_Couleur(tableau_couleur[clic], couleur):
                    print "bonne couleur"
                else:
                    print  "mauvaise couleur"
            except Exception:
                    print "Erreur"
