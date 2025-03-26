import pygame
import random
from pygame.sprite import Sprite

class Enemy(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.image = pygame.image.load("assets/enemy.bmp")  # Asegúrate de tener esta imagen
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, self.settings.anchura - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = self.settings.velocidad_enemigo

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > self.settings.altura:
            self.kill()
