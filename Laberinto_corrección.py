import os
import readchar
import random
from typing import List, Tuple


class Juego:
    def __init__(self, mapa: List[List[str]], posicion_inicial: Tuple[int, int], posicion_final: Tuple[int, int]):
        self.mapa = mapa
        self.posicion_inicial = posicion_inicial
        self.posicion_final = posicion_final

    def screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print()
        for row in self.mapa:
            print(''.join(row))

    def main_loop(self):
        px, py = self.posicion_inicial
        self.mapa[py][px] = 'P'

        self.screen()

        while (px, py) != self.posicion_final:
            key = readchar.readkey()

            x, y = 0, 0
            if key == readchar.key.UP:
                x, y = -1, 0
            elif key == readchar.key.DOWN:
                x, y = 1, 0
            elif key == readchar.key.LEFT:
                x, y = 0, -1
            elif key == readchar.key.RIGHT:
                x, y = 0, 1

            new_px, new_py = px + x, py + y

            if 0 <= new_px < len(self.mapa) and 0 <= new_py < len(self.mapa[0]) and self.mapa[new_px][new_py] != '#':
                self.mapa[px][py] = '.'
                px, py = new_px, new_py
                self.mapa[px][py] = 'P'

                self.screen()
                print(px, py)

            if new_px == self.posicion_final[1] and new_py == self.posicion_final[1]:
                break

        print('Final, final')