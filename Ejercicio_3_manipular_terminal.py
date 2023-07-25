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


   



    


    
    


   




            


