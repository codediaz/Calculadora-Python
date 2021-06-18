""" 
Realizado por: Sergio Díaz F.
Fecha: 16/06/2021

"""
#Library Math
import math
import os

#* Estructura
def Universidad_Intro():
    print(" "*66)
    print("="*66)
    print(" "*15 + " Universidad Politécnica Salesiana ")
    print(" "*25 + " Calculadora ")
    print("="*66)
    print( " Bienvenido!, a continuación escoge la opción que desees realizar: ")
    print(" "*66)   
    
    

def menu_principal():
    print(" "*5+ "1. Operaciones Básicas" )
    print(" "*5+ "2. Operaciones Avanzadas" )
    print(" "*5+ "3. Salir" )
    


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
           
     3. Multiplicación      4. División 
     
     5. Regresar al menú principal""")
    print(" ") 
    opcbasic = input("     Opción: ")
    print(" ")
    while(opcbasic!='5'):
        
        if(opcbasic=='1'):
            sumar()
            print(" ")
        elif(opcbasic=='2'):
            restar()
            print(" ")
        elif(opcbasic=='3'):
            multiplicar()
            print(" ")
        elif(opcbasic=='4'):
            dividir()
            print(" ")
                  
        else:
            print(" "*20+"+-----------------------------+") 
            print(" "*20+"| Escoja una opción correcta! |") 
            print(" "*20+"+-----------------------------+")   
        return()
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
    print(" ")
    a = int(input("     Primer Numero: "))
    b = int(input("     Segundo Numero: ")) 
    result1 = a + b 
    print(" ")
    print("     El resultado de {} + {} es: {} ".format(a,b,result1))
     

def restar():
    print(" ")
    print("     Inserte 2 números") 
    print(" ")
    a = int(input("     Primer Numero: "))
    b = int(input("     Segundo Numero: ")) 
    result1 = a - b 
    print(" ")
    print("     El resultado de {} - {} es: {} ".format(a,b,result1))
    
    
def multiplicar():
    print(" ")
    print("     Inserte 2 números") 
    print(" ")
    a = int(input("     Primer Numero: "))
    b = int(input("     Segundo Numero: ")) 
    result1 = a * b 
    print(" ")
    print("     El resultado de {} * {} es: {} ".format(a,b,result1))
    
def dividir():
    print(" ")
    print("     Inserte 2 números")
    print(" ") 
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
def despedida():
    print(" "*10+"+--------------------------------------+")

    print(" "*10+ "| Gracias por utilizarme, hasta luego! |") 

    print(" "*10+"+--------------------------------------+") 
    
    print(" ")


Universidad_Intro()
menu_principal()
print(" ")
opinicial = input("     Opcion: ")
print(" ")
while (opinicial!= 'Salir'):
        
    if (opinicial == '1'):
        operacionesbasicas()
    elif(opinicial == '2'): 
        operacionesavanzadas()
    elif(opinicial == '3' ):
        despedida()
        exit()
    else:
        print(" "*20+"+-----------------------------+") 
        print(" "*20+"| Escoja una opción correcta! |") 
        print(" "*20+"+-----------------------------+") 
    print(" ")
    print("="*66)
    print(" "*21 + " Menú Principal ")
    print("="*66)
    print(" ")
    menu_principal()
    print(" ")
    opinicial = input("     Opcion: ")
    print(" ")
os.system("cls")





        
