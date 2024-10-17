print("Bienvenido")
a=2
print(a)
b=5.4
print(b)
c="Clase de seguridad"
print(c)
# este simbolo representa un comentario

''' 
Esta seccion es multilinea
'''
d=a+b
print(d)
print(a+b)
print(a-b)
print(a*b)
print(a/b)

# CONDICIONALES(SINTAXIS)
edad = 24
if edad > 18:
    print("Mayor de edad")
else:
    print("Menor de edad")
# DECLARACIÓN DE MULTIPLES VARIABLES
e,f,g=3,8,9
print((e+f)*g)

imprimir=True
if imprimir:
    print("El valor de la operacion es: ",(e+f)*g)
else:
    print("No esta permitido imprimir")
    
# SALTO DE LINE USANDO LA MISMA VARIABLE    
h=1+2+3+4+5+\
6+7+8
print(h)
i=(1+2+3+4+5+
   6+7+8)    
print(i)      

# CREAR FUNCIONES
def suma(j,k):
    # print(j+k)
    return(j+k)

def resta(j,k):
    return(j-k)

def multiplicacion(j,k):
    return(j*k)

def divisor(j,k):
    return(j/k)
print(suma(8,9))
print(resta(8,9))
print(multiplicacion(8,9))
print(divisor(8,9))
# DECLARAR VARIABLES
l=56;m=64;n=49

import keyword
print(keyword.kwlist)          