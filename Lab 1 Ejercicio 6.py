# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 14:52:29 2020

@author: Joaco
"""
"""
# - Variables

ValorA = 1 
ValorB = 3

saludo = "Hola Mundo"
print (saludo)
suma = ValorA + ValorB
print (suma)

nombre = "Joaquin"
Resultado = ValorB*nombre
print (Resultado)"""

#Ejercicio 

print ("Por favor ingrese el valor del paquete de frutas")
fruta = int(input())
print ("Por favor ingrese el valor del paquete de verdura")
verdura = int(input())
print ("Por favor ingrese el valor del paquete de granos")
granos = int(input())
print ("Ingrese su presupuesto")
presupuesto = int(input())
print ("los precios de los productos son",fruta, verdura, granos, "y su presupuesto es", presupuesto)


def funcion(x,y,z):
  if(((x-3) + (y-2) + (z-5)) < presupuesto):
      print("Usted es un buen comprador")
  elif (((x-3) + (y-2) + (z-5))== presupuesto):
      print("Cuidado esta en su limite de presupuesto")
  else:
     print("Regrese cuando tenga mas presupuesto")
     
funcion (fruta,verdura,granos)
    
       
    
    
    