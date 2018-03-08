#! /usr/bin/env python
import os

def cargarLaberinto():
	laberinto = []
	fila = []
	i=0
	
	archivo = open( "matriz.txt", "r" )
	
	for line in archivo.readlines():
		fila = list(line)
		fila.pop()
		fila.pop()

		while fila.count(',') !=0: #busca y retira las comas en la lista
			fila.remove(',')
		
		for valor in fila:#Remplaza los 1's y 0's por *'s y espacios
			if( valor == '0'):
				fila[i] = ' * '
			else:
				fila[i]= '   '
			print fila[i],
			i += 1
		laberinto.append( fila )

		print '\n'
		i = 0
	print '\n\n' 
	print laberinto
	filas = len(laberinto)	
	z = laberinto[0]
	columnas = len(z)
	print filas, columnas

cargarLaberinto()
