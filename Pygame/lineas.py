#importar las librerias de pygame y sys, esta ultima nos ayudara a cerrar la ventana
import pygame, sys
from pygame.locals import * 

pygame.init()#inicializa el modulo de pygame
ventana = pygame.display.set_mode((400,300))#crea un objeto de tipo superficie
pygame.display.set_caption("Hola Mundo")#Mensaje en la superficie

#Creando un color
color = pygame.Color(70,80,150)

#Funcion para dibujar lineas 
#('objeto superficie', 'color de linea', 'coordenadas iniciales', 'coordenadas finales','grosor de linea')
pygame.draw.line(ventana,color,(60,80),(160,100),8)

#visualizar saturacion en color r,g,b
print color.r
print color.g
print color.b

while True:#Mantiene la ventana abierta con un loop infinito
	for event in pygame.event.get():#Captura los eventos en la ventana
		if event.type == QUIT:#Si el usuario presiona en 'x' cerrar
			pygame.quit()#Cierra el modulo de pygame
			sys.exit()#Cierra la ventana
	
	pygame.display.update()#Mantiene la ventana actualizada