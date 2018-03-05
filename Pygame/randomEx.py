import pygame, sys
from pygame.locals import * #importar las librerias de pygame y sys, esta ultima nos ayudara a cerrar la ventana
from random import randint

pygame.init()#inicializa el modulo de pygame
ventana = pygame.display.set_mode((500,500))#crea un objeto de tipo superficie
pygame.display.set_caption("Hola Mundo")#Mensaje en la superficie

mi_imagen = pygame.image.load("img/megaman.png") #ruta de imagen
posX = randint(10,100)
posY  = randint(10,100)

ventana.blit(mi_imagen,(posX,posY))

while True:#Mantiene la ventana abierta con un loop infinito
	for event in pygame.event.get():#Captura los eventos en la ventana
		if event.type == QUIT:#Si el usuario presiona en 'x' cerrar
			pygame.quit()#Cierra el modulo de pygame
			sys.exit()#Cierra la ventana
	
	pygame.display.update()#Mantiene la ventana actualizada