import pygame

#Clase para el Jugador
class Jugador(pygame.sprite.Sprite):
	def __init__(self,ancho,alto):
		pygame.sprite.Sprite.__init__(self)
		self.imagenJugador = pygame.image.load('img/player.png')
		self.rect = self.imagenJugador.get_rect()
		
		self.maxDer = ancho
		self.maxFon = alto
		
		self.rect.left = 60 
		self.rect.top = 120
		
		self.Vida = True
		
		self.velocidad = 60		
		
	def movimientoDerecha(self):
		self.__movimiento()
		self.rect.right += self.velocidad
		self.__movimiento()
		
	def movimientoIzquierda(self):
		self.__movimiento()
		self.rect.left -= self.velocidad
		self.__movimiento()
		
	def movimientoArriba(self):
		self.__movimiento()
		self.rect.top -= self.velocidad
		self.__movimiento()
		
	def movimientoAbajo(self):
		self.__movimiento()
		self.rect.bottom += self.velocidad
		self.__movimiento()
		
	def __movimiento(self):
		if self.Vida == True:
			if self.rect.left <= 0:
				self.rect.left = 0
			elif self.rect.right > self.maxDer:
				self.rect.right = self.maxDer
			elif self.rect.top <= 0:
				self.rect.top = 0
			elif self.rect.bottom > self.maxFon:
				self.rect.bottom = self.maxFon
				
	def comportamiento(self, tiempo):
		self.__movimiento()
	
	def dibujar(self,superficie):
		superficie.blit(self.imagenJugador, self.rect)