#! /usr/bin/env python
import pygame, sys,os
from Clases import Jugador
from Clases import Muro
from pygame.locals import * #importar las librerias de pygame y sys, esta ultima nos ayudara a cerrar la ventana
#-------------------------VARIABLES GLOBALES-----------------------------------
ancho = 900#ancho de la ventana
alto = 900#alto de la ventana
jugador = Jugador(ancho,alto)#creacion del objeto jugador
laberinto = []#matriz de 1's y 0's que definen al laberinto
fila = []#lista auxiliar
archivo = open( "file/matriz.txt", "r" )#archivo que contiene la informacion del laberinto
listaMuros = []#lista de todos los muros con su posicion
#-------------------------FIN DE LAS VARIABLES GLOBALES-------------------------

def cargarArchivo():#Funcion que lee el archivo txt	con la forma del laberinto
	for line in archivo.readlines():
		fila = list(line)
		fila.pop()

		while fila.count(',') != 0: #busca y retira las comas en la lista
			fila.remove(',')
		
		print fila		
		laberinto.append( fila )
		
		
def cargarLaberinto():
	posx = 0
	posy = 0
	i=0
	
	cargarArchivo()		
	alto = len(laberinto) * 60
	fila = laberinto[0]
	ancho = len(fila) * 60	
	print ancho
		
	while i < (alto/60):
		fila = laberinto[i]
		for valor in fila:
			if valor == '0':				
				muro = Muro(posx,posy)
				posx += 60
				listaMuros.append(muro)
			else:
				posx += 60
		posx = 0
		posy += 60
		i += 1
		
	


	
def MazeRunner():
	pygame.init()#inicializa el modulo de pygame	
	cargarLaberinto()
	ventana = pygame.display.set_mode((ancho,alto))#crea un objeto de tipo superficie
	pygame.display.set_caption("Maze Runner")#Mensaje en la superficie
	colorFondo = (255,0,0)
	pygame.mixer.music.load('sounds/megamanX4Volcano.mp3')
	pygame.mixer.music.play(3)
	reloj = pygame.time.Clock()	
	salida = pygame.image.load("img/salida.png")
	entrada = pygame.image.load("img/entrada.png")
	
	enJuego = True
	
	while enJuego:#Mantiene la ventana abierta con un loop infinito
		
		if jugador.rect.right == 900 and jugador.rect.top == 60:
			enJuego = False
			print "Salida"
		reloj.tick(60)
		
		ventana.fill(colorFondo)
		tiempo = pygame.time.get_ticks()/1000
		ventana.blit(salida,(840,60))
		ventana.blit(entrada,(60,120))
	
		for event in pygame.event.get():#Captura los eventos en la ventana
			if event.type == QUIT:#Si el usuario presiona en 'x' cerrar
				pygame.quit()#Cierra el modulo de pygame
				sys.exit()#Cierra la ventana
				
			if enJuego == True:
				for muro in listaMuros:
							if (muro.rect.centerx + 60)==jugador.rect.centerx and muro.rect.centery ==jugador.rect.centery:
								muro.visible = True
							elif (muro.rect.centerx - 60)==jugador.rect.centerx  and muro.rect.centery ==jugador.rect.centery:
								muro.visible = True
							elif (muro.rect.centery + 60)==jugador.rect.centery  and muro.rect.centerx ==jugador.rect.centerx:
								muro.visible = True
							elif (muro.rect.centery - 60)==jugador.rect.centery  and muro.rect.centerx ==jugador.rect.centerx:
								muro.visible = True								
				if event.type == pygame.KEYDOWN:
					if event.key == K_LEFT:
						jugador.movimientoIzquierda()
						for muro in listaMuros:
							if jugador.rect.colliderect(muro.rect):
								jugador.movimientoDerecha()
					elif event.key == K_RIGHT:
						jugador.movimientoDerecha()
						for muro in listaMuros:
							if jugador.rect.colliderect(muro.rect):
								jugador.movimientoIzquierda()		
							
					elif event.key == K_UP:
						jugador.movimientoArriba()
						for muro in listaMuros:
							if jugador.rect.colliderect(muro.rect):
								jugador.movimientoAbajo()
							
					elif event.key == K_DOWN:
						jugador.movimientoAbajo()
						for muro in listaMuros:
							if jugador.rect.colliderect(muro.rect):
								jugador.movimientoArriba()
							
					elif event.key == K_SPACE:
						pygame.quit()
						sys.exit()

		if len(listaMuros) > 0:
			for muro in listaMuros:
				 if muro.visible:
					muro.dibujar(ventana)

		jugador.dibujar(ventana)	
		jugador.comportamiento(tiempo)
		
		pygame.display.update()#Mantiene la ventana actualizada
			
MazeRunner()
