#! /usr/bin/env python
import pygame

#Clase para desierto
class Desierto(pygame.sprite.Sprite):
	def __init__(self,posx, posy):
		pygame.sprite.Sprite.__init__(self)
		self.imagenDesierto = pygame.image.load('img/desierto.jpg')
		self.rect = self.imagenDesierto.get_rect()
			
		self.rect.top = posy
		self.rect.left = posx
		
	def dibujar(self,superficie):
		superficie.blit(self.imagenDesierto, self.rect)