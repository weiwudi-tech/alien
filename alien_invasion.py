import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.clock=pygame.time.Clock()
        self.settings=Settings()
        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.bg_color=self.settings.bg_color
        self.ship=Ship(self)
        self.bullets=pygame.sprite.Group()
        self.aliens=pygame.sprite.Group()
        self._create_fleet()

    def _create_alien(self,x_position):
        new_alien=Alien(self)
        new_alien.x=x_position
        new_alien.rect.x=new_alien.x
        self.aliens.add(new_alien)

        
    def _create_fleet(self):
        #设置外星人间距
        alien=Alien(self)
        alien_width=alien.rect.width
        current_x=alien_width
        while current_x < (self.settings.screen_width-2*alien_width):
            self._create_alien(current_x)
            current_x+=2*alien_width


    
    def _check_keydown_events(self,event):
        if event.key==pygame.K_d:
            self.ship.moving_right=True
        elif event.key==pygame.K_a:
            self.ship.moving_left=True
        elif event.key==pygame.K_w:
            self.ship.moving_up=True
        elif event.key==pygame.K_s:
            self.ship.moving_down=True
        elif event.key==pygame.K_q:
            sys.exit()
        elif event.key==pygame.K_SPACE:
            self._fire_bullet()
            self.ship.image=pygame.image.load("image/state(2).png")


    def _check_keyup_event(self,event):
        if event.key==pygame.K_d:
            self.ship.moving_right=False
        elif event.key==pygame.K_a:
            self.ship.moving_left=False
        elif event.key==pygame.K_w:
            self.ship.moving_up=False
        elif event.key==pygame.K_s:
            self.ship.moving_down=False
        elif event.key==pygame.K_SPACE:
            self.ship.image=pygame.image.load("image/state(1).png")
        
                


    def _check_events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type==pygame.KEYUP:
                self._check_keyup_event(event)
                

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        pygame.display.flip()


    def _fire_bullet(self):
        new_bullet=Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        #更新子弹位置
        self.bullets.update()
        #删除消失的子弹
        for bullet in self.bullets.copy():
                if bullet.rect.bottom<=0:
                    self.bullets.remove(bullet)
        
    
    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self._update_bullets()     
            self.clock.tick(60)
    #输入背景音乐
    file=r"NGGYU.mp3"
    pygame.mixer.init()
    track=pygame.mixer.music.load(file)
    pygame.mixer.music.play()



if __name__=="__main__":
    ai=AlienInvasion()
    ai.run_game()