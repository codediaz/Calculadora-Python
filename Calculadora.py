""" 
Realizado por: Sergio Díaz F.
Fecha: 16/06/2021

"""
#Library Math
import math
import os

#* Estructura
print(" "*66)
print("="*66)
print(" "*15 + " Universidad Politécnica Salesiana ")
print(" "*25 + " Calculadora ")
print("="*66)
print( " Bienvenido!, a continuación escoge la opción que desees realizar: ")
print(" "*66)
print(" "*5+ "1. Operaciones Básicas" )
print(" "*5+ "2. Operaciones Avanzadas" )
print(" "*5+ "3. Salir" )
print(" ")
opinicial = input("     Opcion: ")
print(" ")


#* Funciones Básicas
def operacionesbasicas():
    print(" ")
    print("="*66)
    print(" "*21 + " Operaciones Básicas ")
    print("="*66)
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
    
 
#* Funciones avanzadas
def operacionesavanzadas():
    print(" ")
    print("="*66)
    print(" "*21 + " Operaciones Avanzadas ")
    print("="*66)
    print(" ")
    print("Escoje la operación a realizar:")
    print(" ")
    print("""     1. Suma               2.Resta 
           
     3.Multiplicación      4. División """)
    
    print(" ") 
    
            

#* Operaciones Básicas   
 
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
        print(" ")
        print("     Indefinido: No existe la división para {}".format(b))
    
#* Operaciones avanzadas
def potencia(a,b):
    pot = math.pow(a,b)
    return pot 

def raizcuadrada(a):
    sqr = math.sqrt(a)
    return sqr


while (opinicial!='3'):
    if (opinicial == '1'):
        operacionesbasicas()
    elif(opinicial == '2'): 
        operacionesavanzadas()
    elif(opinicial == '3' ):
        break
    else:
        print(" "*5+"+-----------------------------+") 
        print("     | Escoja una opción correcta! |") 
        print(" "*5+"+-----------------------------+") 
    print(" ")
    opinicial = input("     Opcion: ")
    print(" ")
    
    
print(" "*10+"+--------------------------------------+")

print(" "*10+ "| Gracias por utilizarme, hasta luego! |") 

print(" "*10+"+--------------------------------------+") 



