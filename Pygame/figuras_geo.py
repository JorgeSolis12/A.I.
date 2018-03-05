import pygame, sys
from pygame.locals import * #importar las librerias de pygame y sys, esta ultima nos ayudara a cerrar la ventana

pygame.init()#inicializa el modulo de pygame
ventana = pygame.display.set_mode((400,300))#crea un objeto de tipo superficie
pygame.display.set_caption("Hola Mundo")#Mensaje en la superficie

pygame.draw.circle(ventana,(8,70,120),(80,90),20)
pygame.draw.rect(ventana,(8,70,120),(0,0,100,50))
pygame.draw.polygon(ventana,(255,70,120),((140,0),(291,106),(237,277),(56,277),(0,106)))

while True:#Mantiene la ventana abierta con un loop infinito
	for event in pygame.event.get():#Captura los eventos en la ventana
		if event.type == QUIT:#Si el usuario presiona en 'x' cerrar
			pygame.quit()#Cierra el modulo de pygame
			sys.exit()#Cierra la ventana
	
	pygame.display.update()#Mantiene la ventana actualizada