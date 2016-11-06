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
		self.weight = 20
		self.pos = (50, 80)
		self.reproLimit = 30
		self.vect = (random.randrange(10), random.randrange(10)) 
		Being.beingCreated += 1

# class for ground tiles
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
	
 	# Game clock
	pygame.time.delay(100) 
	
	# Creation of the first generation
	gen = [Being() for i in range(10)]
	print(repro(gen))

	# Creation of the window
	pygame.init()
	window = pygame.display.set_mode((640, 480))
	pygame.display.set_caption("Pygame Test")

	# Test for printing a circle
	DISPLAYSURF = pygame.display.set_mode()
	pygame.draw.circle(DISPLAYSURF, (255, 255, 255), (150, 250), 30)

	# Update the window
	pygame.display.flip()

	# Infinite loop
	booleanCondition = 1
	while booleanCondition:


if __name__ == '__main__':
	main() 
