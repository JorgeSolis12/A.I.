import pygame, sys
from pygame.locals import * #importar las librerias de pygame y sys, esta ultima nos ayudara a cerrar la ventana
#variables globales
ancho = 900
alto = 480

class naveEspacial(pygame.sprite.Sprite):
	"""Clase para las naves"""
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.ImagenNave = pygame.image.load('img/nave.jpg')
		
		self.rect = self.ImagenNave.get_rect()
		self.rect.centerx = ancho/2
		self.rect.centery = alto-30
		
		self.listaDisparo = []
		self.Vida = True

	def disparar(self):
		pass
	
	def dibujar(self, superficie):
		superficie.blit(self.ImagenNave, self.rect)
	
def SpaceInvader():
	pygame.init()#inicializa el modulo de pygame
	ventana = pygame.display.set_mode((ancho,alto))#crea un objeto de tipo superficie
	pygame.display.set_caption("Space Invader")#Mensaje en la superficie
	
	ImagenFondo = pygame.image.load("img/Fondo.jpg")
	
	jugador = naveEspacial()
	
	while True:#Mantiene la ventana abierta con un loop infinito
		for event in pygame.event.get():#Captura los eventos en la ventana
			if event.type == QUIT:#Si el usuario presiona en 'x' cerrar
				pygame.quit()#Cierra el modulo de pygame
				sys.exit()#Cierra la ventana
		
		ventana.blit(ImagenFondo, (0,0))
		jugador.dibujar(ventana)
		pygame.display.update()#Mantiene la ventana actualizada
			
SpaceInvader()