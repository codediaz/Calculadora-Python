""" 
Realizado por: Sergio Díaz F.
Fecha: 16/06/2021

"""
#Library Math
import math

#* Estructura
print("="*65)
print(" "*10 + " Universidad Politécnica Salesiana ")
print(" "*20 + " Calculadora ")
print("="*65)
print( " Bienvenido!, a continuación escoge la opción que desees realizar: ")
print(" "*65)
print(" "*5+ "1. Operaciones Básicas" )
print(" "*5+ "2. Operaciones Avanzadas" )
print(" "*65)
opinicial = input(" "*5+"Opcion: ")



#* Funciones Básicas

def sumar(a,b):
    return a + b 

def restar(a ,b):
    return a - b 

def multiplicar(a,b):
    return a*b

#* Funciones avanzadas

def potencia(a,b):
    pot = math.pow(a,b)
    return pot 
