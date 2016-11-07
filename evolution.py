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
		self.color = 'BLUE'
		self.weight = 20
		self.pos = (50, 80)
		self.reproLimit = 30
		self.vect = (random.randrange(10), random.randrange(10)) 
		Being.beingCreated += 1

# Class for ground tiles
class Tiles:
	def __init__(self):
		self.type = "grass"
		self.food = 20
		self.growing = 1

# Window information
info = pygame.display.Info()
sw = info.current_w
sh = info.current_h
		
# Function for self-reproduction
def repro(listBeing):
	for i in range(len(listBeing)):
		print(listBeing[i].weight)
   
 def main():
	
 	# Game clock
	pygame.time.delay(100) 
	
	# Colors
	BLACK = (0, 0, 0)
	WHITE = (255, 255, 255)
	RED = (255, 0, 0)
	GREEN = (0, 255, 0)
	BLUE = (0, 0, 255)
	
	# Creation of the first generation
	gen = [Being() for i in range(10)]
	#print(repro(gen))

	# Creation of the window
	pygame.init()
	window = pygame.display.set_mode((640, 480))
	windowSurface.fill(WHITE)
	pygame.display.set_caption("Pygame Test")

	# Surface
	DISPLAYSURF = pygame.display.set_mode()

	# Infinite loop
	while True:
		windowSurface.fill(WHITE)
		for i in range(len(gen)):
			pygame.draw.circle(DISPLAYSURF, BLUE, gen[i].pos, gen[i].weight)
			gen[i].pos = ((gen[i].pos[0] + gen[i].vect[0]) % sh, (gen[i].pos[1] + gen[i].vect[0]) % sw)
		
		# Update the window
		pygame.display.flip()
		
		for event in pygame.event.get():
        		if event.type == QUIT:
            			pygame.quit()
           			sys.exit()


if __name__ == '__main__':
	main() 
