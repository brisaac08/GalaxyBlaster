import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, dc_game):
        super().__init__()
        self.screen = dc_game.screen
        self.settings = dc_game.settings
        self.color = self.settings.color_balas

        # Crear una superficie para la bala (image) y rellenarla con color
        self.image = pygame.Surface((self.settings.anchura_balas, self.settings.altura_balas))
        self.image.fill(self.color)

        # Obtener el rectángulo de la bala
        self.rect = self.image.get_rect()
        self.rect.midtop = dc_game.nave.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.velocidad_balas
        self.rect.y = self.y

        if self.rect.bottom < 0:
            self.kill()

    def drawBullet(self):
        self.screen.blit(self.image, self.rect)
