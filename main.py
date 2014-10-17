#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import choix
import initial
import pygame
from pygame.locals import *


pygame.init()

fenetre = pygame.display.set_mode((640, 480))
masque = pygame.image.load("image/masque2.png")

initial.innitialisation(fenetre)

difficulte = 1
if difficulte == 1:
    nb = 4
    pause = 2

for i in choix.couleur(nb):
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
    initial.innitialisation(fenetre)
    time.sleep(0.5)

continuer = 1

while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
        if event.type == MOUSEBUTTONUP and event.button == 1:
            print event.pos
