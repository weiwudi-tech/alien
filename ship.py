import pygame 

class Ship:
    def __init__(self,ai_game):
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.screen_rect=ai_game.screen.get_rect()
        #改变人物图片
        self.image=pygame.image.load("image/state(1).png")
        self.rect=self.image.get_rect()

        self.rect.midbottom=self.screen_rect.midbottom
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)
        
        
        #移动标志位
        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False

    def update(self):
        if self.moving_right and self.x<self.settings.screen_width-70:
            self.x += self.settings.ship_speed
        if self.moving_left and self.x>0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.y>0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.y<self.settings.screen_height-70:
            self.y += self.settings.ship_speed
        

        self.rect.x=self.x
        self.rect.y=self.y

    def blitme(self):
        self.screen.blit(self.image,self.rect)