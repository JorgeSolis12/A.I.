#! /usr/bin/env python
import pygame

#Clase para la tierra
class Tierra(pygame.sprite.Sprite):
	def __init__(self,posx, posy):
		pygame.sprite.Sprite.__init__(self)
		self.imagenTierra = pygame.image.load('img/tierra.jpg')
		self.rect = self.imagenTierra.get_rect()
			
		self.rect.top = posy
		self.rect.left = posx
		
	def dibujar(self,superficie):
		superficie.blit(self.imagenTierra, self.rect)