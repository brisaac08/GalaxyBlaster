import pygame
import sys
import random
import json

from settings import Settings
from ship import Ship
from bullet import Bullet
from enemy import Enemy

class GalaxyBlaster:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.anchura, self.settings.altura))
        self.fondo = pygame.image.load(self.settings.fondo)
        self.fondo = pygame.transform.scale(self.fondo, (self.settings.anchura, self.settings.altura))
        pygame.display.set_caption("Galaxy Blaster")
        self.clock = pygame.time.Clock()

        self.nave = Ship(self)
        self.balas = pygame.sprite.Group()
        self.enemigos = pygame.sprite.Group()
        self.balas_enemigas = pygame.sprite.Group()

        self.juego_activo = False
        self.tiempo_inicio = 0
        self.tiempo_supervivencia = 0
        self.eliminaciones = 0
        self.record = self.cargar_record()
        self.fuente = pygame.font.Font(None, 36)
        
    def cargar_record(self):
        try:
            with open("record.json", "r") as file:
                record = json.load(file)
                # Asegurar que todas las claves existen
                record.setdefault("mejor_tiempo", 0)
                record.setdefault("mejor_bajas", 0)
                record.setdefault("mejor_puntaje", 0)
                return record
        except (FileNotFoundError, json.JSONDecodeError):
            return {"mejor_tiempo": 0, "mejor_bajas": 0, "mejor_puntaje": 0}


    def guardar_record(self):
        puntaje = self.tiempo_supervivencia * 10 + self.eliminaciones * 50
        if puntaje > self.record["mejor_puntaje"]:
            self.record = {"mejor_tiempo": self.tiempo_supervivencia, "mejor_bajas": self.eliminaciones, "mejor_puntaje": puntaje}
            with open("record.json", "w") as file:
                json.dump(self.record, file)

    def mostrar_menu(self):
        fuente = pygame.font.Font(None, 50)
        while True:
            self.screen.fill((0, 0, 0))
            titulo = fuente.render("Bienvenido a Galaxy Blaster", True, (255, 255, 255))
            iniciar = fuente.render("1. Iniciar Juego", True, (255, 255, 255))
            record = fuente.render("2. Ver Récord", True, (255, 255, 255))
            salir = fuente.render("3. Salir", True, (255, 255, 255))
            self.screen.blit(titulo, (200, 150))
            self.screen.blit(iniciar, (250, 250))
            self.screen.blit(record, (250, 300))
            self.screen.blit(salir, (250, 350))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        return True
                    elif event.key == pygame.K_2:
                        self.mostrar_record()
                    elif event.key == pygame.K_3:
                        sys.exit()

    def mostrar_record(self):
        fuente = pygame.font.Font(None, 50)
        while True:
            self.screen.fill((0, 0, 0))
            titulo = fuente.render("Récord del Juego", True, (255, 255, 255))
            tiempo = fuente.render(f"Mejor Tiempo: {self.record['mejor_tiempo']}s", True, (255, 255, 255))
            bajas = fuente.render(f"Mejor Bajas: {self.record['mejor_bajas']}", True, (255, 255, 255))
            puntaje = fuente.render(f"Mejor Puntaje: {self.record['mejor_puntaje']}", True, (255, 255, 255))
            volver = fuente.render("Presiona cualquier tecla para volver", True, (255, 255, 255))
            self.screen.blit(titulo, (250, 150))
            self.screen.blit(tiempo, (250, 250))
            self.screen.blit(bajas, (250, 300))
            self.screen.blit(puntaje, (250, 350))
            self.screen.blit(volver, (200, 450))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    return
    
    def generar_enemigo(self):
        if len(self.enemigos) < self.settings.max_enemigos:
            enemigo = Enemy(self)
            self.enemigos.add(enemigo)
            
    def run_game(self):
        self.juego_activo = self.mostrar_menu()
        self.tiempo_inicio = pygame.time.get_ticks()

        while self.juego_activo:
            self.tiempo_supervivencia = (pygame.time.get_ticks() - self.tiempo_inicio) // 1000
            self.verificar_eventos()
            self.nave.update()
            self.balas.update()
            self.enemigos.update()
            self.balas_enemigas.update()
            self.generar_enemigo()
            self.verificar_colisiones()
            self.actualizar_pantalla()
            self.clock.tick(60)
    
    def verificar_colisiones(self):
        impactos = pygame.sprite.groupcollide(self.balas, self.enemigos, True, True)
        self.eliminaciones += len(impactos)
        
        if pygame.sprite.spritecollideany(self.nave, self.enemigos) or pygame.sprite.spritecollideany(self.nave, self.balas_enemigas):
            self.fin_juego()
    
    def fin_juego(self):
        self.guardar_record()
        fuente = pygame.font.Font(None, 75)
        texto = fuente.render("Game Over", True, (255, 0, 0))
        self.screen.blit(texto, (self.settings.anchura//3, self.settings.altura//3))
        pygame.display.flip()
        pygame.time.wait(2000)
        self.__init__()
        self.run_game()
    
    def verificar_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.nave.movimiento_derecha = True
                elif event.key == pygame.K_LEFT:
                    self.nave.movimiento_izquierda = True
                elif event.key == pygame.K_UP:
                    self.nave.movimiento_arriba = True
                elif event.key == pygame.K_DOWN:
                    self.nave.movimiento_abajo = True
                elif event.key == pygame.K_SPACE:
                    self.disparar()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.nave.movimiento_derecha = False
                elif event.key == pygame.K_LEFT:
                    self.nave.movimiento_izquierda = False
                elif event.key == pygame.K_UP:
                    self.nave.movimiento_arriba = False
                elif event.key == pygame.K_DOWN:
                    self.nave.movimiento_abajo = False
        
    
    def disparar(self):
        if len(self.balas) < self.settings.balas_permitidas:
            bala = Bullet(self)
            self.balas.add(bala)
    
    def actualizar_pantalla(self):
        self.screen.blit(self.fondo, (0, 0))
        self.nave.blitme()
        self.balas.draw(self.screen)
        self.enemigos.draw(self.screen)
        self.balas_enemigas.draw(self.screen)

        #mostrar record si el juego está activo
        if self.juego_activo:
            self.mostrar_record_jugador()

        pygame.display.flip()


    
    #muestra el record en pantalla
    def mostrar_record_jugador(self):
        tiempo_texto = self.fuente.render(f"Tiempo: {self.tiempo_supervivencia}", True, (255, 255, 255))
        eliminaciones_texto = self.fuente.render(f"Eliminaciones: {self.eliminaciones}", True, (255, 255, 255))
        puntaje_actual = (self.tiempo_supervivencia * 10) + (self.eliminaciones * 50)
        puntaje_texto = self.fuente.render(f"Puntaje: {puntaje_actual}", True, (255, 255, 255))

        self.screen.blit(puntaje_texto, (10, 90))
        self.screen.blit(tiempo_texto, (10, 10))
        self.screen.blit(eliminaciones_texto, (10, 50))

if __name__ == '__main__':
    juego = GalaxyBlaster()
    juego.run_game()
    pygame.quit()
