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
    print("""     1. Suma               2. Resta 
           
     3. Multiplicación     4. División 
     
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
            print(" "*5+"+-----------------------------+") 
            print(" "*5+"| Escoja una opción correcta! |") 
            print(" "*5+"+-----------------------------+") 
        return()
#* Funciones avanzadas
def operacionesavanzadas():
    print(" ") 
    print(" ")
    print("="*66)
    print(" "*21 + " Operaciones Avanzadas ")
    print("="*66)
    print(" ")
    print("Escoje la operación a realizar:")
    print(" ")
    print("""     1. Potencia              2. Raiz Cuadrada
           
     3. Regresar al menú principal """)
    print(" ")
    op_av = input("     Opción:  ")
    print(" ")
    while(op_av != '3'):
        
        if( op_av == '1'):
            potencia()
            print(" ")
        elif( op_av == '2'):
            raizcuadrada()
            print(" ")
        else:
            print(" "*5+"+-----------------------------+") 
            print(" "*5+"| Escoja una opción correcta! |") 
            print(" "*5+"+-----------------------------+") 
        return() 
            
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
def potencia():
    a = int(input("     Numero: "))
    b = int(input("     Potencia: ")) 
    pot = math.pow(a,b)
    print(" ")
    print(" "*5+"El resultado de {}^{} es: {}".format(a,b,pot)) 
    

def raizcuadrada():
     a = float(input("     Numero: "))
     a = round(a,2)
     print(" ")
     if ( a>=0):
         sqr = math.sqrt(a)
         sqr = round(sqr,2)
         print(" "*5+"La raiz cuadrada de {} es: {}".format(a,sqr))
     elif( a < 0): 
         print(" "*5+"La raiz cuadrada de {} no esta definida dentro de los numeros reales".format(a))  
     else:
         print(" "*5+"Sólo números..")
     


def despedida():
    print(" "*5+"+--------------------------------------+")

    print(" "*5+ "| Gracias por utilizarme, hasta luego! |") 

    print(" "*5+"+--------------------------------------+") 
    
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
        print(" "*5+"+-----------------------------+") 
        print(" "*5+"| Escoja una opción correcta! |") 
        print(" "*5+"+-----------------------------+") 
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





        
