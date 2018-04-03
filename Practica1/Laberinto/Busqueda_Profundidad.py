import pygame
from pythonds.graphs import Grafo
class Busqueda_Profundidad(grafo):
	 def __init__(self):
        self.relaciones = {}
     def __str__(self):
        return str(self.relaciones)
 
	def agregar(grafo, elemento):
    	grafo.relaciones.update({elemento:[]})

	def relacionar(grafo, elemento1, elemento2):
	    relacionarUnilateral(grafo, elemento1, elemento2)
	    relacionarUnilateral(grafo, elemento2, elemento1)
	   
	def relacionarUnilateral(grafo, origen, destino):
	    grafo.relaciones[origen].append(destino)

	def profundidad(grafo, elementoInicial, funcion, elementosRecorridos = []):
	    if elementoInicial in elementosRecorridos:
	        return
	    funcion(elementoInicial)
	    elementosRecorridos.append(elementoInicial)
	    for vecino in grafo.relaciones[elementoInicial]:
      	  profundidadPrimero(grafo, vecino, funcion, elementosRecorridos)