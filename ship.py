import pygame


class Ship:
    def __init__(self, dc_game):
        self.screen = dc_game.screen
        self.screen_rect = dc_game.screen.get_rect()

        self.image = pygame.image.load('assets/player.bmp')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.movimiento_derecha = False
        self.movimiento_izquierda = False
        self.movimiento_arriba = False
        self.movimiento_abajo = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.movimiento_derecha:
            self.rect.x += 2
        if self.movimiento_izquierda:
            self.rect.x -= 2
        if self.movimiento_arriba:
            self.rect.y -= 2
        if self.movimiento_abajo:
            self.rect.y += 2