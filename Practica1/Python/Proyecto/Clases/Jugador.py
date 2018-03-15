import pygame

#Clase para el Jugador
class Jugador(pygame.sprite.Sprite):
	def __init__(self,ancho,alto):
		pygame.sprite.Sprite.__init__(self)
		self.imagenJugador = pygame.image.load('img/player.png')
		self.rect = self.imagenJugador.get_rect()
		
		self.maxDer = ancho
		self.maxFon = alto
		
		"""self.imagenA = pygame.image.load('img/Marciano2A.jpg')
		self.imagenB = pygame.image.load('img/Marciano2B.jpg')
		self.listaImagenes = [self.imagenA, self.imagenB]
		self.posImagen = 0
		
		self.imagenJugador = self.listaImagenes[self.posImagen]
		self.rect = self.imagenJugador.get_rect()"""
		
		self.rect.left = 60 
		self.rect.top = 60
		
		self.Vida = True
		
		self.velocidad = 60		
		#self.tiempoCambio = 1
		
	"""def movimientoDerecha(self,mover):
		if mover == True:
			self.velocidad = 0
			self.rect.right += self.velocidad
			self.velocidad = 60
		else:
			self.rect.right += self.velocidad
			self.__movimiento()
		
	def movimientoIzquierda(self,mover):
		if mover == True:
			self.velocidad = 0
			self.rect.left -= self.velocidad
			self.velocidad = 60
		else:
			self.rect.left -= self.velocidad
			self.__movimiento()
		
	def movimientoArriba(self,mover):
		if mover == True:
			self.velocidad = 0
			self.rect.top -= self.velocidad
			self.velocidad = 60
		else:
			self.rect.top -= self.velocidad
			self.__movimiento()
		
	def movimientoAbajo(self,mover):
		if mover == True:
			self.velocidad = 0
			self.rect.bottom += self.velocidad
			self.velocidad = 60
		else:
			self.rect.bottom += self.velocidad
			self.__movimiento()"""

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
			elif self.rect.right > self.maxDer:
				self.rect.right = self.maxDer
			elif self.rect.top <= 0:
				self.rect.top = 0
			elif self.rect.bottom > self.maxFon:
				self.rect.bottom = self.maxFon			
				
	def comportamiento(self, tiempo):
		self.__movimiento()

		"""if self.tiempoCambio == tiempo:
			self.posImagen += 1
			self.tiempoCambio += 1
			
			if self.posImagen > len(self.listaImagenes)-1:
				self.posImagen = 0"""
	
	def dibujar(self,superficie):
		superficie.blit(self.imagenJugador, self.rect)
		#self.imagenJugador = self. listaImagenes[self.posImagen]
		#superficie.blit(self.imagenJugador, self.rect)
