import time

from config import MODO_VISUAL

def pausar(segundos):
    # Realiza una pausa solo si está activado el modo visual
    if MODO_VISUAL:
        time.sleep(segundos)
