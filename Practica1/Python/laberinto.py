import pygame, sys
from pygame.locals import * #importar las librerias de pygame y sys, esta ultima nos ayudara a cerrar la ventana
#variables globales
ancho = 500
alto = 500

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

def cargarLaberinto():
	laberinto = []
	fila = []
	i=0
	
	archivo = open( "matriz.txt", "r" )
	
	for line in archivo.readlines():
		fila = list(line)
		fila.pop()
		fila.pop()
		while fila.count(',') !=0: #busca y retira las comas en la lista
			fila.remove(',')
		
		laberinto.append( fila )
		i = 0
	
def SpaceInvader():


	z= x[0]

	print z
	
	filas = len(x)	
	columnas = len(z)
	print filas, columnas

	pygame.init()#inicializa el modulo de pygame
	ventana = pygame.display.set_mode((ancho,alto))#crea un objeto de tipo superficie
	pygame.display.set_caption("Laberinto")#Mensaje en la superficie
	
	ImagenFondo = pygame.image.load("img/Fondo.jpg")
	
	jugador = naveEspacial()
	
	while True:#Mantiene la ventana abierta con un loop infinito
		for event in pygame.event.get():#Captura los eventos en la ventana
			if event.type == QUIT:#Si el usuario presiona en 'x' cerrar
				pygame.quit()#Cierra el modulo de pygame
				sys.exit()#Cierra la ventana
		
		ventana.blit(ImagenFondo, (0,0))
		#jugador.dibujar(ventana)
		pygame.display.update()#Mantiene la ventana actualizada
			
SpaceInvader()
