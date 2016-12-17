import pygame
import random
# from random import randrange, uniform
import time
# from time import delay
import math
# from math import sin, cos, radian, e
from pygame.locals import *

# Class for genetic
class Being:
	#beingCreated = 0
	def __init__(self):
		#self.serialNb = Being.beingCreated 
		#self.name = 'default_name'
		self.color = (random.randrange(0, 255), random.randrange(0, 50), random.randrange(0, 255))
		self.weight = 10
		self.pos = (random.randrange(20, 280), random.randrange(20, 280))
		self.reproLimit = random.randrange(15, 30)
		self.speed = random.uniform(0, 2)
		self.theta = random.randrange(0, 360)
		self.ratio = random.uniform(0, 1)
		#Being.beingCreated += 1

# Class for ground tiles
class Tiles:
	def __init__(self):
		self.color = [0, 100, 0]

# Function for self-reproduction
def repro(listBeing):
	for i in range(len(listBeing)):
		print(listBeing[i].weight)

# Function returning tile coordinate where a Being is 
def zoneMap(position, map_x, map_y, screen_width, screen_height):
	return [int(position[0] * map_x / screen_width), int(position[1] * map_y / screen_height)]

# Calculate radius for a Being weigth
def weightToR(weight):
	#return (weight / math.pi)**(1/2)
	return (weight)**(2/3)

# Normal distribution function
def NFunction(x, mu, theta2):
	return (1 / (2 * theta2 * math.pi)) * math.e**-((x-mu)**2 / (2*theta2))

# Print stats for a Being
def printStats(gen, i):
	print("color: ",gen[i].color)
	print("weight: ",gen[i].weight)
	print("position: ",gen[i].pos)
	print("reproLimit: ",gen[i].reproLimit)
	print("speed: ",gen[i].speed)
	print("theta: ",gen[i].theta)
	print("ratio: ",gen[i].ratio)
	return 0 

#-----------------------------------------------------------------------------------------------	
   
def main():
	
	# Colors
	BLACK = (0, 0, 0)
	WHITE = (255, 255, 255)
	RED = (255, 0, 0)
	GREEN = (0, 255, 0)
	BLUE = (0, 0, 255)
	
	# Creation of the map
	map_x = 10
	map_y = 10
	gameMap = [[Tiles() for j in range(map_y)] for i in range(map_x)]

	# Creation of the window
	pygame.init()
	tileSize = 30
	screen_width = map_x * tileSize
	screen_height = map_y * tileSize
	window = pygame.display.set_mode((screen_width, screen_height))
	pygame.display.set_caption("Pygame Test")

	# Creation of the first generation
	gen = [Being() for i in range(10)]

	# Surface
	DISPLAYSURF = pygame.display.set_mode()

	# Infinite loop
	while True:
		
		# Draw Tiles
		for i in range(map_y):
			for j in range(map_x):

				# Food generation
				#if gameMap[i][j].color[1] <= 110:
					gameMap[i][j].color[1] += 50 * NFunction(gameMap[i][j].color[1] / 10, 5, 4)
					tempColorTile = [gameMap[i][j].color[0], int(gameMap[i][j].color[1]), gameMap[i][j].color[2]]
					pygame.draw.rect(DISPLAYSURF, tempColorTile, (i * screen_width / map_x, j * screen_width / map_x, screen_width / map_x - 1, screen_height / map_y - 1))
					
		# Draw Being
		for i in range(len(gen)):
			posTemp = (int(gen[i].pos[0]), int(gen[i].pos[1]))
			pygame.draw.circle(DISPLAYSURF, gen[i].color, posTemp, int(weightToR(gen[i].weight)))
			
			# Horizontal border verification (x) 
			if not (weightToR(gen[i].weight) <= int(gen[i].pos[0] + gen[i].speed * math.cos(math.radians(gen[i].theta))) <= screen_width - weightToR(gen[i].weight)):
				gen[i].theta = 180 - gen[i].theta
			
			# Vertical border verification (y)
			if not (weightToR(gen[i].weight) <= int(gen[i].pos[1] + gen[i].speed * math.sin(math.radians(gen[i].theta))) <= screen_height - weightToR(gen[i].weight)):
				gen[i].theta = 360 - gen[i].theta

			# Calculate new position
			gen[i].pos = (gen[i].pos[0] + gen[i].speed * math.cos(math.radians(gen[i].theta)), gen[i].pos[1] + gen[i].speed * math.sin(math.radians(gen[i].theta)))
			gps = zoneMap(gen[i].pos, map_x, map_y, screen_width, screen_height)

			# Calculate weight Being
			metabolism = 0.1 * gen[i].weight + gen[i].speed
			eat = gameMap[gps[0]][gps[1]].color[1] * 0.04
			gen[i].weight += (eat - metabolism)

			# Harvest food Tile
			gameMap[gps[0]][gps[1]].color[1] -= eat

			# Reproduction
			if gen[i].weight >= gen[i].reproLimit:
				gen.insert(i + 1, Being())
				gen[i + 1].color = gen[i].color
				gen[i + 1].pos = gen[i].pos
				gen[i + 1].speed = gen[i].speed
				gen[i + 1].reproLimit = gen[i].reproLimit
				gen[i + 1].weight = int((1 - gen[i].ratio) * gen[i].weight)
				gen[i].weight *= gen[i].ratio
				#printStats(gen, i)
				#printStats(gen, i + 1)
				#break
			
			# Clear corpses
			if gen[i].weight <= 0:
				del gen[i]
				print(len(gen))
				# if len(gen) == 0:
				# 	gen = [Being() for i in range(1)]
				break

		# Update the window(gen[i].pos)]
		pygame.display.flip()
		DISPLAYSURF.fill(BLACK)

		# Game clock
		pygame.time.delay(20) 
	
#-----------------------------------------------------------------------------------------------

	# Keyboard events management				       
	for event in pygame.event.get():
		if (event.type == QUIT):
			pygame.quit()
			sys.exit()

if __name__ == '__main__':
	main() 