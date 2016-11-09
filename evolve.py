import pygame
import random
# from random import randrange, uniform
import time
# from time import delay
import math
# from math import sin, cos, radian
from pygame.locals import *

# Class for genetic
class Being:
	beingCreated = 0
	def __init__(self):
		self.serialNb = Being.beingCreated 
		self.name = 'default_name'
		self.color = (random.randrange(0,255), random.randrange(0,50), random.randrange(0,255))
		self.weight = 10
		self.pos = (random.randrange(30,600), random.randrange(30,400))
		self.reproLimit = 30
		self.speed = random.uniform(0, 3)
		self.theta = random.randrange(0, 360)
		Being.beingCreated += 1

# Class for ground tiles
class Tiles:
	def __init__(self):
		self.color = (0, 255, 0)
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
	
	# Creation of the map
	map_x = 10
	map_y = 10
	gameMap = [[Tiles() for j in range(map_x)] for i in range(map_y)]

	# Creation of the window
	pygame.init()
	screen_width = 500
	screen_height = 500
	window = pygame.display.set_mode((screen_width, screen_height))
	pygame.display.set_caption("Pygame Test")

	# Surface
	DISPLAYSURF = pygame.display.set_mode()

	# Infinite loop
	
	while True:
		# Draw Tiles
		for i in range(map_y):
			for j in range(map_x)
				pygame.draw.rect(DISPLAYSURF, gameMap[i][j].color, (i * screen_width / map_x, j * screen_width / map_x, screen_width / map_x - 2, screen_height / map_y - 2))

				# Rect
				# first number = top left rectangle x coordinate
				# second number = top left rectangle y coordinate
				# third number = width of rectangle
				# fourth number = length of rectangle
		
		
		
		
		# Draw Being
		for i in range(len(gen)):
			posTemp = (int(gen[i].pos[0]), int(gen[i].pos[1]))
			pygame.draw.circle(DISPLAYSURF, gen[i].color, posTemp, gen[i].weight)
			
			# Horizontal border verification (x) 
			if not (gen[i].weight <= int(gen[i].pos[0] + gen[i].speed * math.cos(math.radians(gen[i].theta))) <= screen_width - gen[i].weight):
				gen[i].theta = 180 - gen[i].theta
			
			# Vertical border verification (y)
			if not (gen[i].weight <= int(gen[i].pos[1] + gen[i].speed * math.sin(math.radians(gen[i].theta))) <= screen_height - gen[i].weight):
				gen[i].theta = 360 - gen[i].theta

			# Calculate new position
			gen[i].pos = (gen[i].pos[0] + gen[i].speed * math.cos(math.radians(gen[i].theta)), gen[i].pos[1] + gen[i].speed * math.sin(math.radians(gen[i].theta)))
		
		# Update the window
		pygame.display.flip()
		DISPLAYSURF.fill(BLACK)

		# Game clock
		pygame.time.delay(20) 
	
	# Keyboard events management				       
	for event in pygame.event.get():
		if (event.type == QUIT):
			pygame.quit()
			sys.exit()


if __name__ == '__main__':
	main() 