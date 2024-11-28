from constants import *
import game
import music
import rankings as ranks
import pygame

pygame.init()

def principal():
    """Maneja la pantalla de inicio.
    Dentro de un bucle while se le asignan los valores que debe tener el menu de inicio, 
    se  pone un titulo con dicha funcion y se pega usando `pantalla.blit`, 
    luego se crea `texto_inicio` de la misma forma que el anterior y por ultimo se llama al modulo `rankings`
    para que cargue el puntaje mas alto guardado."""
    while True:
        pantalla.fill(VERDE_CLARO)
        fuente = pygame.font.SysFont("Arial", 40)
        texto_titulo = fuente.render("Snake Game", True, BLANCO)
        pantalla.blit(texto_titulo, (ANCHO // 2 - texto_titulo.get_width() // 2, ALTO // 4))

        fuente = pygame.font.SysFont("Arial", 20)
        texto_inicio = fuente.render("Presiona cualquier tecla para jugar", True, BLANCO)
        pantalla.blit(texto_inicio, (ANCHO // 2 - texto_inicio.get_width() // 2, ALTO // 2))

        rankings = ranks.cargar_rankings()
        texto_puntaje_alto = fuente.render(f"Puntaje mas alto: {rankings['puntaje_alto']}", True, BLANCO)
        pantalla.blit(texto_puntaje_alto, (ANCHO // 2 - texto_puntaje_alto.get_width() // 2, ALTO // 1.5))

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()                                                                                                                                                                                                                                                      
            elif evento.type == pygame.KEYDOWN:
                music.reproducir_musica()
                game.ciclo_juego() 


principal()