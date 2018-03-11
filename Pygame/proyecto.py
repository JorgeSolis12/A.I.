import pygame, sys
from pygame.locals import * #importar las librerias de pygame y sys, esta ultima nos ayudara a cerrar la ventana
from random import randint
#variables globales
listaEnemigo = []
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
		
		self.velocidad = 20
		
		self.sonidoDisparo = pygame.mixer.Sound('sounds/disparo.wav')
	
	def movimientoDerecha(self):
		self.rect.right += self.velocidad
		self.__movimiento()
		
	def movimientoIzquierda(self):
		self.rect.left -= self.velocidad
		self.__movimiento()
		
	def __movimiento(self):
		if self.Vida == True:
			if self.rect.left <= 0:
				self.rect.left = 0
			elif self.rect.right > 900:
				self.rect.right = 900
	
	def disparar(self,x,y):
		miProyectil = Proyectil(x,y, "img/disparoa.jpg", True)
		self.listaDisparo.append(miProyectil)
		self.sonidoDisparo.play()
	
	def dibujar(self, superficie):
		superficie.blit(self.ImagenNave, self.rect)
	
class Proyectil(pygame.sprite.Sprite):	
	def __init__(self, posx, posy, ruta, personaje):
		pygame.sprite.Sprite.__init__(self)
		
		self.imageProyectil = pygame.image.load(ruta)
		
		self.rect = self.imageProyectil.get_rect()
		
		self.velocidadDisparo = 5
		
		self.rect.top = posy
		self.rect.left = posx
		
		self.disparoPersonaje = personaje
		
	def trayectoria(self):
		if self.disparoPersonaje == True:
			self.rect.top = self.rect.top - self.velocidadDisparo
		else:
			self.rect.top = self.rect.top + self.velocidadDisparo
	
	def dibujar(self,superficie):
		superficie.blit(self.imageProyectil, self.rect)

class Invasor(pygame.sprite.Sprite):	
	def __init__(self, posx, posy, distancia, imagenUno, imagenDos):
		pygame.sprite.Sprite.__init__(self)
		
		self.imagenA = pygame.image.load(imagenUno)
		self.imagenB = pygame.image.load(imagenDos)
		#self.imagenB = pygame.image.load('img/MarcianoB.jpg')
		
		self.listaImagenes = [self.imagenA, self.imagenB]
		self.posImagen = 0
		
		self.imagenInvasor = self.listaImagenes[self.posImagen]
		self.rect = self.imagenInvasor.get_rect()
		
		self.listaDisparo = []
		self.velocidad = 20
		self.rect.top = posy
		self.rect.left = posx
		
		self.rangoDisparo = 5
		self.tiempoCambio = 1
		
		self.derecha = True
		self.contador = 0
		self.MaxDescenso = self.rect.top + 40
		
		self.limiteDerecha = posx + distancia
		self.limiteIzquierda = posx - distancia
		
	def dibujar(self,superficie):
		self.imagenInvasor = self. listaImagenes[self.posImagen]
		superficie.blit(self.imagenInvasor, self.rect)
	
	def comportamiento(self, tiempo):
		self.__movimientos()
		
		self.__ataque()
		if self.tiempoCambio == tiempo:
			self.posImagen += 1
			self.tiempoCambio += 1
			
			if self.posImagen > len(self.listaImagenes)-1:
				self.posImagen = 0
	
	def __movimientos(self):
		if self.contador  < 3:
			self.__movimientoLateral()
		else:
			self.__descenso()
			
	def __descenso(self):
		if self.MaxDescenso == self.rect.top:
			self.contador = 0
			self.MaxDescenso = self.rect.top +40
		else:
			self.rect.top += 1
			
	def __movimientoLateral(self):
		if self.derecha == True:
			self.rect.left += self.velocidad
			if self.rect.left > self.limiteDerecha:
				self.derecha = False
				self.contador += 1
		else:
			self.rect.left -= self.velocidad
			if self.rect.left < self.limiteIzquierda:
				self.derecha = True
	
	def __ataque(self):
		if (randint(0,100) < self.rangoDisparo ):
			self.__disparo()
	
	def __disparo(self):
		x,y = self.rect.center
		miProyectil = Proyectil(x,y, "img/disparob.jpg", False)
		self.listaDisparo.append(miProyectil)

def cargarEnemigos():
	posx = 100
	for x in rage(1,5):
		enemigo = Invasor(posx,100,40,'img/MarcianoA.jpg','img/MarcianoB.jpg')
		listaEnemigo.append(enemigo)
		posx += 200
	
	for x in rage(1,5):
		enemigo = Invasor(posx,0,40,'img/Marciano2A.jpg','img/Marciano2B.jpg')
		listaEnemigo.append(enemigo)
		posx += 200
	
	for x in rage(1,5):
		enemigo = Invasor(posx,-100,40,'img/Marciano3A.jpg','img/Marciano3B.jpg')
		listaEnemigo.append(enemigo)
		posx += 200

def SpaceInvader():
	pygame.init()#inicializa el modulo de pygame
	ventana = pygame.display.set_mode((ancho,alto))#crea un objeto de tipo superficie
	pygame.display.set_caption("Space Invader")#Mensaje en la superficie
	
	ImagenFondo = pygame.image.load("img/Fondo.jpg")
	
	pygame.mixer.music.load('sounds/megamanX4Volcano.mp3')
	pygame.mixer.music.play(3)
	
	jugador = naveEspacial()
	cargarEnemigos()
	
	enJuego = True
	
	reloj = pygame.time.Clock()
	
	while True:#Mantiene la ventana abierta con un loop infinito
		reloj.tick(60)
		
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
					elif event.key == K_s:
						x,y = jugador.rect.center
						jugador.disparar(x,y)
		
		ventana.blit(ImagenFondo, (0,0))
		
		jugador.dibujar(ventana)

		if len(jugador.listaDisparo) > 0:
			for x in jugador.listaDisparo:
				x.dibujar(ventana)
				x.trayectoria()
				
				if x.rect.top <-10:
					jugador.listaDisparo.remove(x)
		
		if listaEnemigo > 0:
			for enemigo in listaEnemigo:
				enemigo.comportamiento(tiempo)
				enemigo.dibujar(ventana)		
				if len(enemigo.listaDisparo) > 0:
					for x in enemigo.listaDisparo:
						x.dibujar(ventana)
						x.trayectoria()
						
						if x.rect.top >900:
							enemigo.listaDisparo.remove(x)
				
		pygame.display.update()#Mantiene la ventana actualizada
			
SpaceInvader()