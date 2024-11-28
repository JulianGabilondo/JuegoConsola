from constants import *
import pygame
import random
import music
import game

def dibujar_bordes():
    """Utiliza draw.rect para dibujar los limites del mapa"""
    grosor_borde = 20
    pygame.draw.rect(pantalla, VERDE, (0, 0, ANCHO, ALTO ), grosor_borde)

def dibujar_serpiente(cuerpo_serpiente):
    """Utiliza un bucle for para iterar sobre la lista `cuerpo_serpiente` y luego se usa blit para dibujar la textura"""
    for segmento in cuerpo_serpiente:
        pantalla.blit(piel, segmento)

def dibujar_manzana(manzana, comida):
    """En el argumento `comida` establece las coordenadas mediante una tupla, 
    para poder pegar la imagen usando `pantalla.blit`"""
    # Esto desempaqueta las coordenadas de la comida
    x, y = comida
    ancho_manzana, alto_manzana = manzana.get_size() # Obtiene el tamanio de la imagen
    offset_x = (10 - ancho_manzana) // 2 # Se usa el tamanio obtenido en get_size para centrar la imagen en el bloque
    offset_y = (10 - alto_manzana) // 2
    pantalla.blit(manzana, (x + offset_x, y + offset_y)) #Se dibuja la imagen ajustada con el desplazamiento

def mover_serpiente(cuerpo_serpiente:list, direccion:str) -> list:
    """Se utilizan condicionales para determinar a donde se moverá la serpiente,
    luego retorna la lista `cuerpo_serpiente` con los valores actualizados"""
    cabeza = cuerpo_serpiente[0]
    if direccion == 'ARRIBA':
        nueva_cabeza = (cabeza[0], cabeza[1] - 10)
    elif direccion == 'ABAJO':
        nueva_cabeza = (cabeza[0], cabeza[1] + 10)
    elif direccion == 'IZQUIERDA':
        nueva_cabeza = (cabeza[0] - 10, cabeza[1])
    elif direccion == 'DERECHA':
        nueva_cabeza = (cabeza[0] + 10, cabeza[1])
    
    # Insertamos la nueva cabeza y eliminamos la cola
    cuerpo_serpiente = [nueva_cabeza] + cuerpo_serpiente[:-1]
    return cuerpo_serpiente

def generar_comida(cuerpo_serpiente:list) -> tuple:
    """Utiliza un bucle while para generar de manera constante y aleatoria la comida"""
    while True:
        comida_x = random.randint(MARGEN_BORDES // 10, (ANCHO - MARGEN_BORDES - 10) // 10) * 10
        comida_y = random.randint(MARGEN_BORDES // 10, (ALTO - MARGEN_BORDES - 10) // 10) * 10
        comida = (comida_x, comida_y)
        if comida not in cuerpo_serpiente:
            return comida

def verificar_colision(cuerpo_serpiente:list, puntaje:int) -> bool:
    """Utiliza una condicional para determinar si la lista `cuerpo_serpiente` colisiona con los bordes del mapa o consigo misma"""
    cabeza = cuerpo_serpiente[0]
    # Colisión con los bordes
    if cabeza[0] < MARGEN_BORDES or cabeza[0] >= ANCHO - MARGEN_BORDES or cabeza[1] < MARGEN_BORDES or cabeza[1] >= ALTO - MARGEN_BORDES:
        music.reproducir_sonido_muerte()
        game.mostrar_game_over(puntaje)
        return True
    
    # Colisión consigo mismo verifica si la cabeza de la serpiente se encuentra en cualquier parte de de su cuerpo
    if cabeza in cuerpo_serpiente[1:]:
        music.reproducir_sonido_muerte()
        game.mostrar_game_over(puntaje)
        return True
        
    return False

def dibujar_bordes():
    """Utiliza bucles for para dibujar los bordes superior inferior, izquierda y derecha usando una textura de muro""" 
    for x in range(0, ANCHO, 20):  
        pantalla.blit(muro_imagen, (x, 0))
    for x in range(0, ANCHO, 20):  
        pantalla.blit(muro_imagen, (x, ALTO - 20))
    for y in range(0, ALTO, 20):  
        pantalla.blit(muro_imagen, (0, y))
    for y in range(0, ALTO, 20):  
        pantalla.blit(muro_imagen, (ANCHO - 20, y))