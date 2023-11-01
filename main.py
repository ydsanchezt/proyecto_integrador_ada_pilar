from Funciones import main_loop, string_to_matrix
from Laberinto_corrección import Juego
from Encapsulado_juego_POO import Juego_Archivo

name = input ('por favor ingrese su nombre: ') 
print(f'{name}, Bienvenido al juego del laberinto !!!')

laberinto = """.############
....#.......#
###.#.###.###
#...#...#...#
#.#####.#.#.#
#...#.#.#.#.#
#.#.#.#####.#
#.#.....#.#.#
#.###.###.#.#
#.#.........#
###.#####.###
#.......#...#
###########.#"""

mapa = string_to_matrix(laberinto)

def main():
    main_loop(mapa, (0, 0), (11, 12))
    path_a_mapas = 'mapas'  
    juego = Juego_Archivo(path_a_mapas)
    juego.main_loop()

if __name__ == "__main__":
    main()
