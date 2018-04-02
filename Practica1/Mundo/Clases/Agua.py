#! /usr/bin/env python
import pygame

#Clase para agua
class Agua(pygame.sprite.Sprite):
	def __init__(self,posx, posy):
		pygame.sprite.Sprite.__init__(self)
		self.imagenAgua = pygame.image.load('img/agua.jpg')
		self.rect = self.imagenAgua.get_rect()
			
		self.rect.top = posy
		self.rect.left = posx
		
	def dibujar(self,superficie):
		superficie.blit(self.imagenAgua, self.rect)