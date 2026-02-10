import random

print("Piedra, Papel o tijera")
opciones = ["piedra" , "papel" , "tijera"]
jugador = input("Elige piedra, papel o tijera: ").lower()
print(" Tu elegiste:" , jugador)
computadora = random.choice(opciones)
print( "La computadora eligió:" , computadora)
if jugador == computadora:
    print("Empate")
elif jugador == "piedra" and computadora == "tijera":
    print("Ganaste!!!")
elif jugador == "tijera" and computadora == "papel":
    print("Ganaste!!!")
elif jugador == "papel" and computadora == "piedra":
    print("Ganaste!!!")
else:
    print("Perdistee wajajaj")