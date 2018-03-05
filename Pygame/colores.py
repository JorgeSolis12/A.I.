#Rojo, Verde y Azul
#RGB(120,50,50)

import pygame, sys
from pygame.locals import * #importar las librerias de pygame y sys, esta ultima nos ayudara a cerrar la ventana

color=(0,140,60)#Tupla con valores RGB
color_dos=pygame.Color(255,120,9)#creando color de otra forma

pygame.init()#inicializa el modulo de pygame
ventana = pygame.display.set_mode((400,300))#crea un objeto de tipo superficie
pygame.display.set_caption("Hola Mundo")#Mensaje en la superficie

while True:#Mantiene la ventana abierta con un loop infinito
	ventana.fill(color_dos)
	for event in pygame.event.get():#Captura los eventos en la ventana
		if event.type == QUIT:#Si el usuario presiona en 'x' cerrar
			pygame.quit()#Cierra el modulo de pygame
			sys.exit()#Cierra la ventana
	
	pygame.display.update()#Mantiene la ventana actualizada