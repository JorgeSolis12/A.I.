#! /usr/bin/env python
import pygame

#Clase para el Muro
class Muro(pygame.sprite.Sprite):
	def __init__(self,posx, posy):
		pygame.sprite.Sprite.__init__(self)
		self.imagenMuro = pygame.image.load('img/muro.png')
		self.rect = self.imagenMuro.get_rect()
			
		self.rect.top = posy
		self.rect.left = posx
		
	def dibujar(self,superficie):
		superficie.blit(self.imagenMuro, self.rect)