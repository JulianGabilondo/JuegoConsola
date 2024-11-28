import pygame

def reproducir_sonido_muerte():
    """reproduce el sonido cuando el jugador pierde el juego, controlando el volumen"""
    sonido = pygame.mixer.Sound('assets/sounds/sonido_muerte.wav')
    sonido.set_volume(0.1)
    sonido.play()

def reproducir_musica():
    """Reproduce la musica de fondo del juego, controlando el volumen"""
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.load('assets/sounds/alphys.flac')
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)