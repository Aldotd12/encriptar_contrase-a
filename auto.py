# Practica en donde se hace el uso de variables globales
# y/o variables locales haciendo la sumulacion de un auto

# Auto
# ->Avanzar -> llave
# ->Frenar
# ->Apagar
# ->Encender -> llave
# ->GirarIzq
# ->GirarDer

llave = False
avanzar=True

def insertar_llave():
    global llave
    llave = True
    print("Llave insertada listo para encender.")
def encender():
    if llave:
        print("El auto está encendido listo para avanzar.")
    else:
        print("No puedes encender el auto sin la llave.")
def avanzar():
    if llave:
        print("El auto está avanzando.")
    else:
        print("No puedes avanzar si el auto no esta encendido.")
def frenar():
    if avanzar:
        print("El auto está frenando.")
    else:
        print("No puedes frenar el auto si no esta avanzando.")
def girar_der():
    if llave:
        print("El auto está girando a la derecha.")
    else:
        print("No puedes girar el auto si el auto no esta encendido.")
def girar_izq():
    if llave:
        print("El auto está girando a la izquierda.")
    else:
        print("No puedes girar el auto si o esta encendido.")

def apagar():
    if llave:
        print("El auto está apagado.")
    else:
        print("No puedes apagar el auto si no esta encendido.")

insertar_llave() # Inserta la llave
encender()       # Enciende el auto
avanzar()        # El auto avanza
girar_der()      # Gira el auto a la derecha
girar_izq()      # Gira el auto a la izquierda
frenar()         # El auto frena
apagar()         # Apaga el auto    
