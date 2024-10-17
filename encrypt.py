import bcrypt

def encriptar_contraseña():
    while True:
        # Pedir la contraseña al usuario
        contraseña = input("Ingresa la contraseña a encriptar: ").encode('utf-8')
        
        # Generar un salt
        salt = bcrypt.gensalt()
        
        # Encriptar la contraseña
        contraseña_encriptada = bcrypt.hashpw(contraseña, salt)
        
        # Mostrar la contraseña encriptada
        print(f"Contraseña encriptada: {contraseña_encriptada.decode('utf-8')}")
        
        # Preguntar si el usuario quiere continuar
        continuar = input("¿Deseas encriptar otra contraseña? (s/n): ").lower()
        if continuar != 's':
            print("Programa terminado.")
            break

encriptar_contraseña()
