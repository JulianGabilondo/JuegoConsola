from constants import *
import rankings as ranks
import pygame
import snake

def mostrar_game_over(puntaje:int):
    """Se crean fuentes y texto para renderizarlos y luego mostrarlos con `pantalla.blit` cuando el jugador pierde la partida
    Ademas se utiliza un bucle while y condicionales para detectar cuando el jugador presione una tecla"""
    pantalla.fill(NEGRO)
    fuente= pygame.font.SysFont("times new roman", 40)
    texto = fuente.render(f"GAME OVER!!! Puntaje: {puntaje}", True, ROJO )
    pantalla.blit(texto, (ANCHO // 2 - texto.get_width() // 2, ALTO // 3))

    fuente_opciones = pygame.font.SysFont("Arial",20) 
    texto_opciones = fuente_opciones.render("Presiona R para reiniciar o Q para salir", True, BLANCO)
    pantalla.blit(texto_opciones, (ANCHO // 2 - texto_opciones.get_width() // 2, ALTO // 2))

    pygame.display.update()
    pygame.time.delay(2000)
    eleccion = True
    while eleccion:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif evento.key == pygame.K_r:
                    eleccion = False
                    ciclo_juego()

def ciclo_juego():
    """Se determinan los valores del cuerpo de la serpiente, la direccion con la que inicia, generacion de la comida de manera aleatoria y se inicia el puntaje en cero.
    A traves de un bucle while se detectan las teclas presionadas, se actualiza la funcion `dibujar_bordes`,
    se dibuja la serpiente, se detecta su movimiento y ademas se le agrega un segmento, se verifican colisiones,
    se crea la comida, se dibuja y se verifica cuando la serpiente la come, se incrementa el puntaje, se actualiza
    la pantalla y se controla la velocidad del juego"""
    cuerpo_serpiente = [(100, 100), (90, 100), (80, 100)]
    direccion = 'DERECHA'
    comida = snake.generar_comida(cuerpo_serpiente)
    puntaje = 0

    while True:
        pantalla.blit(pasto, (0,0) )
        snake.dibujar_bordes()

        # Detectar eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP and direccion != 'ABAJO':
                    direccion = 'ARRIBA'
                elif evento.key == pygame.K_w and direccion != 'ABAJO':
                    direccion = 'ARRIBA'
                elif evento.key == pygame.K_DOWN and direccion != 'ARRIBA':
                    direccion = 'ABAJO'
                elif evento.key == pygame.K_s and direccion != 'ARRIBA':
                    direccion = 'ABAJO'
                elif evento.key == pygame.K_LEFT and direccion != 'DERECHA':
                    direccion = 'IZQUIERDA'
                elif evento.key == pygame.K_a and direccion != 'DERECHA':
                    direccion = 'IZQUIERDA'
                elif evento.key == pygame.K_RIGHT and direccion != 'IZQUIERDA':
                    direccion = 'DERECHA'
                elif evento.key == pygame.K_d and direccion != 'IZQUIERDA':
                    direccion = 'DERECHA'

        # Mover la serpiente
        cuerpo_serpiente = snake.mover_serpiente(cuerpo_serpiente, direccion)

        # Verificar colisiones
        if snake.verificar_colision(cuerpo_serpiente, puntaje):
            return ranks.guardar_rankings(puntaje)

        # Comer la comida
        if cuerpo_serpiente[0] == comida:
            cuerpo_serpiente.append(cuerpo_serpiente[-1])  # Agregar segmento al cuerpo
            comida = snake.generar_comida(cuerpo_serpiente)  # Generar nueva comida
            puntaje += 10  # Incrementar puntaje

        # Dibujar la serpiente y la comida
        snake.dibujar_serpiente(cuerpo_serpiente)
        snake.dibujar_manzana(manzana, comida)

        # Mostrar puntaje
        fuente = pygame.font.SysFont("Arial", 14)
        texto_puntaje = fuente.render(f"Puntaje: {puntaje}", True, BLANCO)
        pantalla.blit(texto_puntaje, (0, 0))

        # Actualizar la pantalla
        pygame.display.flip()

        # Limitar FPS
        reloj.tick(FPS)