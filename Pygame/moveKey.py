import pygame, sys
from pygame.locals import * #importar las librerias de pygame y sys, esta ultima nos ayudara a cerrar la ventana

pygame.init()#inicializa el modulo de pygame
ventana = pygame.display.set_mode((1500,1000))#crea un objeto de tipo superficie
pygame.display.set_caption("Hola Mundo")#Mensaje en la superficie

mi_imagen = pygame.image.load("img/megaman.png") #ruta de imagen
posX,posY = 200,100 #equivale a posX = 130 posY = 70

velocidad = 5

blanco = (255,255,255)
derecha = True

while True:#Mantiene la ventana abierta con un loop infinito

	ventana.fill(blanco)
	ventana.blit(mi_imagen,(posX,posY))
	for event in pygame.event.get():#Captura los eventos en la ventana
		if event.type == QUIT:#Si el usuario presiona en 'x' cerrar
			pygame.quit()#Cierra el modulo de pygame
			sys.exit()#Cierra la ventana
		elif event.type == pygame.KEYDOWN:
			if event.key == K_LEFT:
				posX -= velocidad
			elif event.key == K_RIGHT:
				posX += velocidad
		elif event.type == pygame.KEYUP:
			if event.key == K_LEFT:
				print "Tecla izquierda liberada"
			elif event.key == K_RIGHT:
				print "Tecla derecha liberada"
	
	pygame.display.update()#Mantiene la ventana actualizada