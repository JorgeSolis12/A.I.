import pygame, sys
from pygame.locals import * #importar las librerias de pygame y sys, esta ultima nos ayudara a cerrar la ventana

pygame.init()#inicializa el modulo de pygame
ventana = pygame.display.set_mode((400,300))#crea un objeto de tipo superficie
pygame.display.set_caption("Hola Mundo")#Mensaje en la superficie

fuente = pygame.font.SysFont("Arial",30)

aux = 1
while True:#Mantiene la ventana abierta con un loop infinito
	ventana.fill((255,255,255))
	tiempo = pygame.time.get_ticks()/1000
	if aux == tiempo:
		aux += 1
		print tiempo
	
	for event in pygame.event.get():#Captura los eventos en la ventana
		if event.type == QUIT:#Si el usuario presiona en 'x' cerrar
			pygame.quit()#Cierra el modulo de pygame
			sys.exit()#Cierra la ventana
			
	contador = fuente.render("Tiempo: "+str(tiempo),0,(120,70,0))	
	ventana.blit(contador,(100,100))
	pygame.display.update()#Mantiene la ventana actualizada