import pygame

muro_imagen = pygame.image.load("assets/images/stone_wall01.png")
muro_imagen = pygame.transform.scale(muro_imagen, (20, 20))

piel = pygame.image.load("assets/images/piel.jpg")
piel = pygame.transform.scale(piel, (10, 10))

pasto = pygame.image.load("assets/images/pasto.jpg")
pasto = pygame.transform.scale(pasto, (600, 400))

manzana = pygame.image.load("assets/images/manzana.png")
manzana = pygame.transform.scale(manzana, (25, 25))

MARGEN_BORDES = 20
ANCHO = 600
ALTO = 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))

icono = pygame.image.load("assets/images/icon.png")
pygame.display.set_icon(icono)
pygame.display.set_caption("Snake Game")

BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)
AMARILLO = (244, 208, 63)
VERDE_CLARO = (46, 204, 113)

# Configuración del reloj (FPS)
reloj = pygame.time.Clock()
FPS = 15