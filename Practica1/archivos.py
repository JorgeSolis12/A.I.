#! /usr/bin/env python

#! /usr/bin/env python
"""import os
x = []
archivo = open("matriz.txt","r") # Abre archivo con el nombre matriz.txt
for line in archivo.readlines():
	while line.count(',') !=0: #busca y retira las comas en la lista
		line.remove(',')
	y = list ([value for value in line.split()])
	x.append( y )
print x
archivo.close(); # cerrar el archivo
"""

import os
#def leer matriz()
archivo = open("matriz.txt","r") # Abre archivo con el nombre matriz.txt

i=0
j=0

lista = []

for linea in archivo.readlines(): #Lee y recorre las lineas del archivo
	lista[i]= list(linea) #la funcion list recibe el objeto linea y retorna una lista a la variable 'lista'
	lista.remove('\n') #Retira los saltos de linea de la lista
	
	while lista.count(',') !=0: #busca y retira las comas en la lista
		lista.remove(',')
		
	for valor in lista:#Remplaza los 1's y 0's por *'s y espacios
		if( valor == '0'):
			lista[i][j] = ' * '
		else:
			lista[i][j]= '   '
		print(lista[i][j])		
		j += 1
		
	print('\n')
	j += 1
	i = 0

# El for es para leer todas las lineas renglon por renglon
archivo.close();
