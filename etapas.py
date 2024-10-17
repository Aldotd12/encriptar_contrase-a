# REALIZAR UN PROGRAMA QUE PERMITA AGREGAR LA EDAD Y QUE INDIQUE
# SI LA PERSONA ES MENOR DE 12 ES NIÑO, SI LA PERSONA ES MAYOR A 
# 12 Y MENOR A 17 ES ADOLECENTE, SI LA PERSONA ES MAYOR A 16 Y MENOR
# A 29 ES JOVEN, SI LA PERSONA ES MAYOR A 29 Y MENOR A 55 ES 
# ADULTO Y SI ES MAYOR A 55 ES DE LA TERCERA EDAD.

def edad():
    edad = int(input("Cual es tu edad:" ))
    if edad < 13:
        print("Es niño")
    elif edad > 12 and edad <= 16:
        print("Es adolecente")
    elif edad >= 17 and  edad <= 29:
        print("Es joven")
    elif edad >= 30  and edad <= 55:
        print("Es adulto")
    else:
        print("Es de la tercera edad")
edad()                            