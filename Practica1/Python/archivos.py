#! /usr/bin/env python
import os
"""def leer matriz()"""
archivo = open("matriz.txt","r") # Abre archivo con el nombre matriz.txt

i=0

for linea in archivo.readlines(): #Lee y recorre las lineas del archivo
	lista = list(linea) #la funcion list recibe el objeto linea y retorna una lista a la variable 'lista'
	lista.remove('\n') #Retira los saltos de linea de la lista
	
	while lista.count(',') !=0: #busca y retira las comas en la lista
		lista.remove(',')
		
	for valor in lista:#Remplaza los 1's y 0's por *'s y espacios
		if( valor == '0'):
			lista[i] = ' * '
		else:
			lista[i] = '   '
		print(lista[i], end='')		
		i += 1
		
	print('\n')
	i=0

# El for es para leer todas las lineas renglon por renglon
archivo.close();
