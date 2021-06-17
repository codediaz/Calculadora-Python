""" 
Realizado por: Sergio Díaz F.
Fecha: 16/06/2021

"""
#Library Math
import math

#* Estructura
print(" "*57)
print("="*57)
print(" "*10 + " Universidad Politécnica Salesiana ")
print(" "*20 + " Calculadora ")
print("="*57)
print(" "*57)
print( " Bienvenido!, a continuación escoge la opción que desees realizar: ")
print(" "*57)
print(" "*5+ "1. Operaciones Básicas" )
print(" "*5+ "2. Operaciones Avanzadas" )
print(" "*57)
opinicial = int(input("     Opcion: "))


#* Funciones Básicas
def operacionesbasicas():
    print(" ")
    print("="*57)
    print(" "*15 + " Operaciones Básicas ")
    print("="*57)
    print(" ")
    print("Escoje la operación a realizar:")
    print(" ")
    print("""     1. Suma               2.Resta 
           
     3.Multiplicación      4. División """)
    
    print(" ") 
    
    opcbasic = int(input("     Opción: ")) 
    print(" ")
    if(opcbasic==1):
        sumar()
        print(" ")
    elif(opcbasic==2):
        restar()
        print(" ")
    elif(opcbasic==3):
        multiplicar()
        print(" ")
    elif(opcbasic==4):
        dividir()
        print(" ")
    
    else:
        print("Mal")    
    
         
       
def sumar():
    print(" ")
    print("     Inserte 2 números") 
    a = int(input("     Primer Numero: "))
    b = int(input("     Segundo Numero: ")) 
    result1 = a + b 
    print(" ")
    print("     El resultado de {} + {} es: {} ".format(a,b,result1))
     

def restar():
    print(" ")
    print("     Inserte 2 números") 
    a = int(input("     Primer Numero: "))
    b = int(input("     Segundo Numero: ")) 
    result1 = a - b 
    print(" ")
    print("     El resultado de {} - {} es: {} ".format(a,b,result1))
    
    
def multiplicar():
    print(" ")
    print("     Inserte 2 números") 
    a = int(input("     Primer Numero: "))
    b = int(input("     Segundo Numero: ")) 
    result1 = a * b 
    print(" ")
    print("     El resultado de {} * {} es: {} ".format(a,b,result1))
    
def dividir():
    print(" ")
    print("     Inserte 2 números") 
    a = int(input("     Primer Numero: "))
    b = int(input("     Segundo Numero: ")) 
    
    if b != 0 :
        result1 = a / b 
        print(" ")
        print("     El resultado de {} / {} es: {} ".format(a,b,result1))
    else:
        print("     Indefinido: No existe la división para {}".format(b))
    

#* Funciones avanzadas

def potencia(a,b):
    pot = math.pow(a,b)
    return pot 

def raizcuadrada(a):
    sqr = math.sqrt(a)
    return sqr


if (opinicial == 1):
    operacionesbasicas()
    



