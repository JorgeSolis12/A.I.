import pygame, sys
from pygame.locals import * #importar las librerias de pygame y sys, esta ultima nos ayudara a cerrar la ventana

pygame.init()#inicializa el modulo de pygame
ventana = pygame.display.set_mode((1500,1000))#crea un objeto de tipo superficie
pygame.display.set_caption("Hola Mundo")#Mensaje en la superficie

mi_imagen = pygame.image.load("img/megaman.png") #ruta de imagen
posX,posY = 130,70 #equivale a posX = 130 posY = 70

velocidad = 1

blanco = (255,255,255)
derecha=True

while True:#Mantiene la ventana abierta con un loop infinito

	ventana.fill(blanco)
	ventana.blit(mi_imagen,(posX,posY))
	for event in pygame.event.get():#Captura los eventos en la ventana
		if event.type == QUIT:#Si el usuario presiona en 'x' cerrar
			pygame.quit()#Cierra el modulo de pygame
			sys.exit()#Cierra la ventana
	
	if derecha == True:
		if posX<1100:
			posX+=velocidad
		else:
			derecha=False
	else:
		if posX>1:
			posX-=velocidad
		else:
			derecha=True
			
	pygame.display.update()#Mantiene la ventana actualizada