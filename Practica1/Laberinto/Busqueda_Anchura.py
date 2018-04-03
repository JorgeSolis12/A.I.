import pygame
from pythonds.graphs import Grafo
class Busqueda_Anchura(grafo):
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
	    
	def anchura(grafo, elementoInicial, funcion, cola = deque(), elementosRecorridos = []):
    if not elementoInicial in elementosRecorridos:
        funcion(elementoInicial)
        elementosRecorridos.append(elementoInicial)
        if(len(grafo.relaciones[elementoInicial]) > 0):
            cola.extend(grafo.relaciones[elementoInicial])
    if len(cola) != 0 :
        anchoPrimero(grafo, cola.popleft(), funcion, cola, elementosRecorridos)   