#!/usr/bin/python
import sys

def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return 0
    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while num > 1: 
            fact *= num 
            num -= 1
        return fact 

if len(sys.argv) > 1:
    num = int(sys.argv[1])
else:
     user_input = input("ingrese un numero para calcular su factorial: ")
     user_input = user_input.replace("!","")
try:
    num = int(user_input)
except valueerror:
       print("por favor, ingrese un numero valido.")
       sys.exit(1)

print(f"Factorial  {num}! es {factorial(num)}") 

