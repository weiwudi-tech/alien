import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.color=self.settings.bullet_color
        #在（0，0）创建子弹，再设置子弹位置
        self.rect=pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop=ai_game.ship.rect.midtop
        #存储子弹位置
        self.y=float(self.rect.y)

    def update(self):
        self.y -=self.settings.bullet_speed
        self.rect.y=self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)