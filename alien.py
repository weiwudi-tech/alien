import pygame
import random
from pygame.sprite import Sprite

A=["image/ship1.bmp","image/ship2.bmp","image/ship3.bmp","image/ship4.bmp"]
class Alien(Sprite):

    def __init__(self,ai_game):
        super().__init__()
        self.screen=ai_game.screen
        self.image=pygame.image.load(random.choice(A))
        self.rect=self.image.get_rect()

        self.rect.x=self.rect.width
        self.rect.y=self.rect.height

        self.x=float(self.rect.x)