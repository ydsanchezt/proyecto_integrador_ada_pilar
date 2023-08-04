import os

def implementar_laberinto(laberinto):
    return [list(filas) for filas in laberinto.strip().split('\n')]

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_loop(mapa, inicio, final):
    px, py = inicio

    def mostrar_mapa():
        limpiar_pantalla()
        mapa[px][py] = 'P'
        for fila in mapa:
            print(''.join(fila))
        mapa[px][py] = '.'

    while (px, py) != final:
        mostrar_mapa()
        tecla = input("Presiona una tecla de flecha (arriba, abajo, izquierda, derecha): ").lower()

        if tecla == "arriba" and px > 0 and mapa[px - 1][py] != '#':
            mapa[px][py] = '.'
            px -= 1
        elif tecla == "abajo" and px < len(mapa) - 1 and mapa[px + 1][py] != '#':
            mapa[px][py] = '.'
            px += 1
        elif tecla == "izquierda" and py > 0 and mapa[px][py - 1] != '#':
            mapa[px][py] = '.'
            py -= 1
        elif tecla == "derecha" and py < len(mapa[0]) - 1 and mapa[px][py + 1] != '#':
            mapa[px][py] = '.'
            py += 1

    mostrar_mapa()
    print("¡LLegaste, por fin!")

if __name__ == "__main__":
  
    laberinto = """
..███████████████████
........█.........█.█
█.█.█.█.█.███████.█.█
█.█.█.█.█...█...█.█.█
█.█.█.█.█.███.███.█.█
█.█.█.█...█...█.█...█
███.█.█.█.█.█.█.█.███
█...█.█.█.█.█.█...█.█
█.█.█████.███.█.███.█
█.█.█.█.█.█...█.█...█
█.█.█.█.█████.███.███
█.█...█...█.█...█...█
█████.███.█.█.█.█.███
█...█.█.......█.....█
█.███.███.█.█████████
█...█.█.█.█.........█
█.███.█.█.███.███.███
█.█.█.....█...█.█...█
█.█.█.███.█████.█.███
█.......█.....█.....
█████████████████████
    """

    inicio = (0, 0)
    final = (7,7)

    mapa = implementar_laberinto(laberinto)
    main_loop(mapa, inicio, final)


