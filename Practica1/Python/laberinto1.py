#! /usr/bin/env python
import pygame, sys,os
from pygame.locals import * #importar las librerias de pygame y sys, esta ultima nos ayudara a cerrar la ventana
from random import randint
#variables globales
ancho  = 870
alto = 660
laberinto = []
fila = []
archivo = open( "matriz.txt", "r" )
listaMuros = []
#listaMuros

class Muro(pygame.sprite.Sprite):

	def __init__(self,posx, posy):
		pygame.sprite.Sprite.__init__(self)
		self.imagenMuro = pygame.image.load('img/muro.png')
		self.rect = self.imagenMuro.get_rect()
			
		self.rect.top = posy
		self.rect.left = posx
		
	def dibujar(self,superficie):
		superficie.blit(self.imagenMuro, self.rect)
		

class Jugador(pygame.sprite.Sprite):
	"""Clase para las naves"""
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		"""self.imagenJugador = pygame.image.load('img/megaman.gif')
		self.rect = self.imagenJugador.get_rect()"""
		
		self.imagenA = pygame.image.load('img/Marciano2A.jpg')
		self.imagenB = pygame.image.load('img/Marciano2B.jpg')
		self.listaImagenes = [self.imagenA, self.imagenB]
		self.posImagen = 0
		
		self.imagenJugador = self.listaImagenes[self.posImagen]
		self.rect = self.imagenJugador.get_rect()
		
		self.rect.centerx = ancho/2
		self.rect.centery = alto/2
		
		self.Vida = True
		
		self.velocidad = 20		
		self.tiempoCambio = 1
		
	def movimientoDerecha(self):
		self.rect.right += self.velocidad
		self.__movimiento()
		
	def movimientoIzquierda(self):
		self.rect.left -= self.velocidad
		self.__movimiento()
		
	def movimientoArriba(self):
		self.rect.top -= self.velocidad
		self.__movimiento()
		
	def movimientoAbajo(self):
		self.rect.bottom += self.velocidad
		self.__movimiento()
		
	def __movimiento(self):
		if self.Vida == True:
			if self.rect.left <= 0:
				self.rect.left = 0
			elif self.rect.right > 900:
				self.rect.right = 900
			elif self.rect.top <= 0:
				self.rect.top = 1
			elif self.rect.bottom > 480:
				self.rect.bottom = 480
				
	def comportamiento(self, tiempo):
		self.__movimiento()

		if self.tiempoCambio == tiempo:
			self.posImagen += 1
			self.tiempoCambio += 1
			
			if self.posImagen > len(self.listaImagenes)-1:
				self.posImagen = 0
	
	def dibujar(self,superficie):
		#superficie.blit(self.imagenJugador, self.rect)
		self.imagenJugador = self. listaImagenes[self.posImagen]
		superficie.blit(self.imagenJugador, self.rect)

def cargarArchivo():
		
	for line in archivo.readlines():
		fila = list(line)
		fila.pop()

		while fila.count(',') != 0: #busca y retira las comas en la lista
			fila.remove(',')
				
		laberinto.append( fila )	
		
def cargarLaberinto():
	posx = 0
	posy = 0
	i=0
	
	cargarArchivo()		
	#alto = len(laberinto) * 66
	fila = laberinto[0]
	#ancho = len(fila) * 87	

	
		
	while i < (alto/66):
		fila = laberinto[i]
		for valor in fila:
			if valor == '0':
				print  valor,
				muro = Muro(posx,posy)
				posx += 87
				listaMuros.append(muro)
			else:
				posx += 87
		posx = 0
		posy += 66
		i += 1
	
		
def MazeRunner():
	pygame.init()#inicializa el modulo de pygame
	cargarLaberinto()
	ventana = pygame.display.set_mode((ancho,alto))#crea un objeto de tipo superficie
	pygame.display.set_caption("Space Invader")#Mensaje en la superficie
	
	colorFondo = (255,255,255)
	pygame.mixer.music.load('sounds/megamanX4Volcano.mp3')
	pygame.mixer.music.play(3)
	
	reloj = pygame.time.Clock()
	jugador = Jugador()	
	enJuego = True
	
	while True:#Mantiene la ventana abierta con un loop infinito
		reloj.tick(60)
		
		ventana.fill(colorFondo)
		
		tiempo = pygame.time.get_ticks()/1000
		
		for event in pygame.event.get():#Captura los eventos en la ventana
			if event.type == QUIT:#Si el usuario presiona en 'x' cerrar
				pygame.quit()#Cierra el modulo de pygame
				sys.exit()#Cierra la ventana
				
			if enJuego == True:
				if event.type == pygame.KEYDOWN:
					if event.key == K_LEFT:
						jugador.movimientoIzquierda()
					elif event.key == K_RIGHT:
						jugador.movimientoDerecha()
					elif event.key == K_UP:
						jugador.movimientoArriba()
					elif event.key == K_DOWN:
						jugador.movimientoAbajo()
		
		if listaMuros > 0:
			for muro in listaMuros:
				muro.dibujar(ventana)	
		
		jugador.dibujar(ventana)	
		jugador.comportamiento(tiempo)
		
		pygame.display.update()#Mantiene la ventana actualizada
			
MazeRunner()