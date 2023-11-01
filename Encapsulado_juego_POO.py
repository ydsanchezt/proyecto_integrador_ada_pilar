import os
import readchar
import random
from functools import reduce
from typing import List, Tuple
from Laberinto_corrección import Juego


class Juego_archivo(Juego):
    def __init__(self, path_a_mapas: str):
        lista_de_mapas = os.listdir(path_a_mapas)
        nombre_archivo = random.choice(lista_de_mapas)
        path_completo = os.path.join(path_a_mapas, nombre_archivo)
        contenido_mapa, posicion_inicial, posicion_final = self.read_map_file(path_completo)
        super().__init__(contenido_mapa, posicion_inicial, posicion_final)
    
    @staticmethod
    def read_map_file(file_path):
        with open(file_path, 'r') as archivo:
            lineas = archivo.readlines()

        mapa_str = reduce(lambda x, y: x + y, lineas)
        mapa_archivo = mapa_str.strip().split('\n')
        dimensiones = list(map(int, mapa_archivo[0].split()))
        contenido_mapa = [list(row) for row in mapa_archivo[1:]]
        posicion_inicial = (dimensiones[0], dimensiones[1])
        posicion_final = (dimensiones[1], dimensiones[2])

        return contenido_mapa, posicion_inicial, posicion_final