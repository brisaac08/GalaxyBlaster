import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet

class GalaxyBlaster:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.anchura, self.settings.altura))
        self.fondo = pygame.image.load(self.settings.fondo)
        self.fondo = pygame.transform.scale(self.fondo, (self.settings.anchura, self.settings.altura))
        pygame.display.set_caption("Galaxy Blaster")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()



    def actualizar_pantalla(self):
        self.screen.blit(self.fondo, (0, 0))
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.drawBullet()
        pygame.display.flip()



    def shopBullets(self):
        if len(self.bullets) < self.settings.balas_permitidas:
            newBullet = Bullet(self)
            self.bullets.add(newBullet)


    def comprobar_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moviento_derecha = True
                    self.ship.rect.x += 2
                elif event.key == pygame.K_LEFT:
                    self.ship.movimiento_izquierda = True
                    self.ship.rect.x -= 2
                elif event.key == pygame.K_UP:
                    self.ship.movimiento_arriba = True
                    self.ship.rect.y -= 2
                elif event.key == pygame.K_DOWN:
                    self.ship.movimiento_abajo = True
                    self.ship.rect.y += 2
                elif event.key == pygame.K_SPACE:
                    self.shopBullets()


            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moviento_derecha = False
                elif event.key == pygame.K_LEFT:
                    self.ship.movimiento_izquierda = False
                elif event.key == pygame.K_UP:
                    self.ship.movimiento_arriba = False
                elif event.key == pygame.K_DOWN:
                    self.ship.movimiento_abajo = False


    def run_game(self):
        while True:
            self.comprobar_eventos()
            self.ship.update()
            self.bullets.update()
            self.actualizar_pantalla()



if __name__ == '__main__':
    dc = GalaxyBlaster()
    dc.run_game()
