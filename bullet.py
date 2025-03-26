import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, dc_game):
        super().__init__()
        self.screen = dc_game.screen
        self.settings = dc_game.settings
        self.color = self.settings.color_balas
        self.rect = pygame.Rect(0, 0, self.settings.anchura_balas, self.settings.altura_balas)
        self.rect.midtop = dc_game.ship.rect.midtop
        
        self.y = float(self.rect.y)
        

    def update(self):
        self.y -= self.settings.velocidad_balas
        self.rect.y = self.y

        if self.rect.bottom < 0:
            self.kill()

    def drawBullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)