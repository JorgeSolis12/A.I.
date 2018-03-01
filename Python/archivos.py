#! /usr/bin/env python
import os
"""def leer matriz()"""
archivo = open("matriz.txt","r") # Abre archivo con el nombre matriz.txt
lista = [][]
for linea in archivo.readlines(): #Lee y recorre las lineas del objeto
	for letra in linea:
			if(letra == "0"):
				print letra
			if(letra == "1"):
				print letra
					
# El for es para leer todas las lineas renglon por renglon
archivo.close();