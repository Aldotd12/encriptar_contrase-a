# BUCLES: While, for, break, continue

# CICLO WHILE
print("******CICLO WHILE******")
x=0
while x<3:
    print(x)
    x+=1   
    
# ciclo for
print("******CICLO FOR******")
for i in range(5):
    print(i)   
# ciclo for implementando salto
print("***********CICLO FOR CON CONTINUE**********")
for i in range(6):
    if i == 4:
        continue
    print(i)
# CICLO WHILE CON INSTRUCCION PARA FINALIZAR UNA EJECUCION
print("****CICLO CON WHILE Y BREAK******")
x=0
while True:
    print(x)
    if x==20:
        break
    x+=1

# MANEJO DE EXEPCIONES ASSERT, TRY, EXCEPT, finally, RAISE
x="10"
valor = None
try:
    valor=int(x)
    b=3
    res=valor+b
except Exception as e:
    print("Error:",e)
finally:
    print("El resultado es: ",res)  
    
    
    
    
# Variables locales, variables globales y nonlocal en python
a=0

def suma_uno():
    global a
    for i in range(6):
        a=a+1
    print(a)    
suma_uno()    
print("Valor de a antes de la función: ",a)   

# Uso de nonlocal
print("*****Uso de nonlocal*****")
def funcion_a():
    x=10
    def funcion_b():
        nonlocal x
        x=20
        print("Valor de x dentro de funcion_b: ",x)
    funcion_b()
    print("funcion_a",x)
funcion_a()    