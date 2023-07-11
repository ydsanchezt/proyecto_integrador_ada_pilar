import keyboard

while True:
    letra = keyboard.read_key()
    print(letra)
      
    if letra == "flecha arriba":
        print("fin")
        break

 