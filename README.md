# 🚀 Galaxy Blaster

¡Bienvenido a **Galaxy Blaster**! Un juego arcade de naves espaciales desarrollado en **Python** con la librería **Pygame**.

---

## 📜 Descripción

Galaxy Blaster es un juego de disparos en el espacio donde el jugador controla una nave y debe enfrentarse a oleadas de enemigos mientras los esquiva y dispara proyectiles.  

El objetivo es **sobrevivir el mayor tiempo posible** y **alcanzar la mayor puntuación** al destruir enemigos. El juego guarda el puntaje más alto registrado.

---

## Menú de inicio

### 🚀 Inicio del juego
Al ejecutar el juego, aparece la pantalla de inicio con las siguientes opciones:

1. Iniciar partida → Comenzar el juego inmediatamente.
2. Ver récord → Mostrar la puntuación más alta guardada.
3. Salir → Cerrar el juego.

Cada número corresponde a la tecla que debe presionar para acceder a esa opción del menú.


## 🎮 Controles

| Acción         |         Tecla         |
|----------------|-----------------------|
| Mover derecha  | ➡️ (Flecha derecha)   |
| Mover izquierda| ⬅️ (Flecha izquierda) |
| Mover arriba   | ⬆️ (Flecha arriba)    |
| Mover abajo    | ⬇️ (Flecha abajo)     |
| Disparar       | Barra espaciadora     |


---

### 🏆 Sistema de puntuación
Cada enemigo destruido suma puntos.

Esquivar ataques enemigos no suma puntos, pero evita que pierdas.

El juego termina cuando algún enemigo choca con tu nave.

La cantidad de puntos se calcula de la siguiente manera: 10 puntos por cada segundo de supervivencia y 50 puntos por cada asesinatos de enemigos.

## 📁 Dónde se guarda el puntaje máximo
El juego almacena el récord del puntaje más alto en un archivo llamado record.json dentro del directorio del juego.

Si el jugador supera la puntuación máxima anterior, el récord se actualiza automáticamente.

La próxima vez que inicies el juego, el puntaje más alto se cargará desde este archivo.


## 🛠️ Pasos para la instalación y ejecución

## 🔽 1. Clonar el repositorio
```sh
git clone https://github.com/brisaac08/GalaxyBlaster.git
cd GalaxyBlaster
```


## 2. Instalar dependencias
Asegúrate de tener Python instalado en tu sistema. 

```sh
py --version
```

Sino está instalado descargalo 


***Recomendado:*** https://www.python.org/downloads/


O por la terminal 

```sh
winget install Python.Python
```

Luego, instala las librerías necesarias con:

```sh
python -m pip install -U pygame==2.5.2
```
Se recomienda la versión **2.5.2** por ser la más eficiente.


### ▶️ 3. Ejecutar el juego
```sh
python galaxyBlaster.py
```

## Documentación de pygames

**Enlace:** https://www.pygame.org/news