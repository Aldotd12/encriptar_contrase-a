def sumar_numeros():
    while True:
        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            suma = num1 * num2
            print(f"La suma de {num1} y {num2} es: {suma}")
        except ValueError:
            print("Por favor, ingresa números válidos.")

        continuar = input("¿Deseas realizar otra suma? (s/n): ").lower()
        if continuar != 's':
            print("Programa terminado.")
            break

sumar_numeros()
