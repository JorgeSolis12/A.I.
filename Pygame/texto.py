import pygame, sys
from pygame.locals import * #importar las librerias de pygame y sys, esta ultima nos ayudara a cerrar la ventana

pygame.init()#inicializa el modulo de pygame
ventana = pygame.display.set_mode((400,300))#crea un objeto de tipo superficie
pygame.display.set_caption("Hola Mundo")#Mensaje en la superficie

mi_fuente = pygame.font.Font(None,30)
mi_texto = mi_fuente.render("Prueba Fuente",0,(200,60,80))

mi_fuente_sistema = pygame.font.SysFont("Arial",30)
mi_texto_sistema = mi_fuente.render("Prueba Fuente Sistema",0,(200,60,80))

while True:#Mantiene la ventana abierta con un loop infinito
	for event in pygame.event.get():#Captura los eventos en la ventana
		if event.type == QUIT:#Si el usuario presiona en 'x' cerrar
			pygame.quit()#Cierra el modulo de pygame
			sys.exit()#Cierra la ventana
	
	ventana.blit(mi_texto,(100,100))
	ventana.blit(mi_texto_sistema,(0,0))
	pygame.display.update()#Mantiene la ventana actualizada