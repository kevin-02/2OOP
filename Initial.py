import pygame
from pygame.locals import *

def initialisation(fenetre):
    vert = pygame.image.load("image/vert.png")
    fenetre.blit(vert, (110,30))

    jaune = pygame.image.load("image/jaune.png")
    fenetre.blit(jaune, (330,30))

    rouge = pygame.image.load("image/rouge.png")
    fenetre.blit(rouge, (110,250))

    bleu = pygame.image.load("image/bleu.png")
    fenetre.blit(bleu, (330,250))

    pygame.display.flip()
