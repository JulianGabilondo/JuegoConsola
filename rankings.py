import os
import json

def cargar_rankings() -> dict:
    """Carga el archivo `rankings.json` que contiene el puntaje mas alto, si el archivo no existe devuelve por defecto puntaje igual a cero"""
    if os.path.exists('rankings.json'):
        with open('rankings.json', 'r') as archivo:
            return json.load(archivo)
    return {"puntaje_alto": 0}

def guardar_rankings(puntaje:int):
    """Guarda el puntaje mas alto en el archivo `rankings.json` actualizandolo si el nuevo puntaje es mas alto que el guardado anteriormente"""
    rankings = cargar_rankings()
    if puntaje > rankings["puntaje_alto"]:
        rankings["puntaje_alto"] = puntaje
        with open('rankings.json', 'w') as archivo:
            json.dump(rankings, archivo)