import pygame
from pygame.locals import *

def input(events):
    ''' Function to handle key events and quit '''
    for event in events:
        if event.type == QUIT:
            quit()
        else:
        	if event.type == KEYDOWN:
                 print(event.key)


pygame.init()

window = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Pygame Test")

DISPLAYSURF = pygame.display.set_mode()
pygame.draw.circle(DISPLAYSURF, (255, 255, 255), (150, 250), 30)



pygame.display.flip()


booleanCondition = 1
while booleanCondition:
   input(pygame.event.get())
   
   
