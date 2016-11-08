import pygame
import random
import time
from pygame.locals import *

# Class that define genetic
class Being:

	beingCreated = 0

	def __init__(self):
		self.serialNb = Being.beingCreated 
		self.name = 'default_name'
		self.color = (random.randrange(50,255), random.randrange(50,255), random.randrange(50,255))
		self.weight = 10
		self.pos = (random.randrange(30,600), random.randrange(30,400))
		self.reproLimit = 30
		self.vect = [random.randrange(-3, 3), random.randrange(-3, 3)] 
		Being.beingCreated += 1

# Class for ground tiles
class Tiles:
	def __init__(self):
		self.type = "grass"
		self.food = 20
		self.growing = 1

# Function for self-reproduction
def repro(listBeing):
	for i in range(len(listBeing)):
		print(listBeing[i].weight)
   
def main():
	
	# Colors
	BLACK = (0, 0, 0)
	WHITE = (255, 255, 255)
	RED = (255, 0, 0)
	GREEN = (0, 255, 0)
	BLUE = (0, 0, 255)
	
	# Creation of the first generation
	gen = [Being() for i in range(10)]

	# Creation of the window
	pygame.init()
	screen_width=640
	screen_height=480
	window = pygame.display.set_mode((screen_width, screen_height))
	
	pygame.display.set_caption("Pygame Test")

	# Surface
	DISPLAYSURF = pygame.display.set_mode()

	# Infinite loop
	while True:
		
		for i in range(len(gen)):
			pygame.draw.circle(DISPLAYSURF, gen[i].color, gen[i].pos, gen[i].weight)
			if not (gen[i].weight <= (gen[i].pos[0] + gen[i].vect[0]) <= screen_width - gen[i].weight):
				gen[i].vect[0] *= -1
			if not (gen[i].weight <= (gen[i].pos[1] + gen[i].vect[1]) <= screen_height - gen[i].weight):
				gen[i].vect[1] *= -1

			gen[i].pos = ((gen[i].pos[0] + gen[i].vect[0]) , (gen[i].pos[1] + gen[i].vect[1]) )
		
		# Update the window
		pygame.display.flip()
		DISPLAYSURF.fill(BLACK)

		# Game clock
		pygame.time.delay(20) 
		
	for event in pygame.event.get():
		if (event.type == QUIT):
			pygame.quit()
			sys.exit()


if __name__ == '__main__':
	main() 
