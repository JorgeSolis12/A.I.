import pygame, sys
from pygame.locals import * #importar las librerias de pygame y sys, esta ultima nos ayudara a cerrar la ventana
from random import randint
#variables
screen_w = 400
screen_h = 300
color = (255,255,255)
lcubito = 0
acubito = 0
#clase deljugador
class jugador(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.imagenJugador = pygame.image.load("img/megaman.png")
		self.rect = self.imagenJugador.get_rect()
		self.rect.centerx = screen_w/2
		self.rect.centery = screen_h-30
		self.velocidad=20

	def dibujar(self, superficie):
		superficie.blit(self.imagenJugador, self.rect)
		
#clase para el laberinto
class maze():
	def _init_(self):
		self.cont = 0
		self.paredx = 0
		self.paredy = 0
		self.listarec = [] #se ocupa para hacer una lista de listas
		#esta la podemos sustituir por nuestra funcion para crear matrices
	def cargaLaberinto():
		archivo = open("matriz.txt","r") # Abre archivo con el nombre matriz.txt
		i=0

		for linea in archivo.readlines(): #Lee y recorre las lineas del archivo
			lista = list(linea) #la funcion list recibe el objeto linea y retorna una lista a la variable 'lista'
			lista.remove('\n') #Retira los saltos de linea de la lista
			lcubito = screen_h/len(linea) #son las variables para el tamano del cubo en y
			acubito =screen_w/15 #igual pero para x, aqui dividelo entre lo que encontraste tu :V no me acuerdo yo de como era :'C
			
			while lista.count(',') !=0: #busca y retira las comas en la lista
				lista.remove(',')
				
			for valor in lista: 
				if( valor == '0'):
					self.listarec.append(pygame.Rect(self.paredx, paredy,lcubito,acubito)) #esto sirve para crear los rectangulos
					self.paredx+=lcubito #esto puede servir para donde se van a colocar
				else:
					self.paredx = lcubito #esto sirve para dejar los espacios
			
			self.paredx = 0 
			self.paredy = acubito	

		# El for es para leer todas las lineas renglon por renglon
		archivo.close();
			

def crear_juego():
	pygame.init()
	ventana = pygame.display.set_mode((screen_w,screen_h))
	pygame.display.set_caption("Practica1")
	fondo = pygame.image.load("img/Fondo.jpg")

	player1 = jugador()
	laberinto = maze()
	enJuego = True

	while True:
		ventana.blit(fondo,(screen_w,screen_h))
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			if enJuego == True:
				if event.type == pygame.KEYDOWN:
					if event.key == K_LEFT:
						player1.rect.left -= velocidad
					
					elif event.key == K_RIGHT:
						player1.rect.right += velocidad

					elif event.key == K_UP:
						player1.rect.up += velocidad

					elif event.key == K_DOWN:
						player1.rect.down -= velocidad

		ventana.blit(fondo, (0,0))
		player1.dibujar(ventana)
		pygame.display.update()

def main():
	crear_juego()
if __name__ == '__main__':
	main()