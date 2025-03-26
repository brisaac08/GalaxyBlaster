class Settings:
    def __init__(self):
        # Configuración de pantalla
        self.anchura = 840
        self.altura = 650
        self.fondo = "assets/background.png"

        # Nave
        self.velocidad_nave = 10  # Velocidad de la nave

        # Configuración de las balas
        self.velocidad_balas = 5  # velocidad de las balas
        self.anchura_balas = 3
        self.altura_balas = 15
        self.color_balas = (0, 0, 255)  # Azul
        self.balas_permitidas = 6  # Máximo de balas activas en pantalla

        # Enemigos
        self.velocidad_enemigo = 2 # Velocidad de los enemigos
        self.max_enemigos = 5 # Cantidad máxima de enemigos en pantalla
        self.spawn_rate = 50 # Cuántos frames esperar antes de generar un enemigo nuevo

        # Configuración de la puntuación
        self.puntos_por_enemigo = 50
