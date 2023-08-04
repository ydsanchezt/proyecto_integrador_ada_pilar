#Parte 1
nombre = input ("por favor ingrese su nombre: ")
print (nombre)
print ("Bienvenido al juego del laberinto " + nombre + ". ¡Muchos exitos, aprende, disfruta, no te detengas! ")

#Parte 2
import keyboard

while True:
    letra = keyboard.read_key()
    print(letra)
      
    if letra == "flecha arriba":
        print("fin")
        break

#Parte 3
import os
def borrar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(número)
número = 0
while número <=50:
    borrar_terminal()
    ingreso_usuario = input( "presione la tecla n para continuar: ")
    if ingreso_usuario == "n":
     número +=1
    else:
        print("Fin")
        break
#Parte 4

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
    final = (10,10)

    mapa = implementar_laberinto(laberinto)
    main_loop(mapa, inicio, final)

