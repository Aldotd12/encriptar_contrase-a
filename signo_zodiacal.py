# PROGRAMA QUE DEPENDIENDO DE TU FECHA DE NACIMIENTO TE DE TU SIGNO ZODIACAL

# Aries: 21 de marzo al 19 de abril
# Tauro: 20 de abril y al 20 de mayo
# Géminis: 21 de mayo al 20 de junio
# Cáncer: 21 de junio al 22 de julio
# Leo: 23 de julio al 22 de agosto
# Virgo: 23 de agosto al 22 de septiembre
# Libra: 23 de septiembre al 22 de octubre
# Escorpio: 23 de octubre al 21 de noviembre
# Sagitario: 22 de noviembre al 21 de diciembre
# Capricornio: 22 de diciembre al 19 de enero
# Acuario: 20 de enero al 18 de febrero
# Piscis: 19 de febrero al 20 de marzo

mes = int(input("INGRESA TU MES DE NACIMIENTO:" ))
dia = int(input("INGRESA TU DIA DE NACIMIENTO:" ))

if mes == 3 and dia >= 21 or mes == 4 and dia <= 19:
    print("Tu signo sodiacal es Aries")
elif mes == 4 and dia >= 20 or mes == 5 and dia <= 20:
    print("Tu signo sodiacal es Tauro")
elif mes == 5 and dia >= 21 or mes == 6 and dia <= 20:
    print("Tu signo sodiacal es Géminis")
elif mes == 6 and dia >= 21 or mes == 7 and dia <= 22:
    print("Tu signo sodiacal es Cáncer")
elif mes == 7 and dia >= 23 or mes == 8 and dia <= 22:
    print("Tu signo sodiacal es Leo")
elif mes == 8 and dia >= 23 or mes == 9 and dia <= 22:
    print("Tu signo sodiacal es Virgo")
elif mes == 9 and dia >= 23 or mes == 10 and dia <= 22:
    print("Tu signo sodiacal es Libra")
elif mes == 10 and dia >= 23 or mes == 11 and dia <= 21:
    print("Tu signo sodiacal es Escorpio")
elif mes == 11 and dia >= 22 or mes == 12 and dia <= 21:
    print("Tu signo sodiacal es Sagitario")
elif mes == 12 and dia >= 22 or mes == 1 and dia <= 19:
    print("Tu signo sodiacal es Capricornio")
elif mes == 1 and dia >= 20 or mes == 2 and dia <= 18:
    print("Tu signo sodiacal es Acuario")
else:
    print("Tu signo sodiacal es Piscis")