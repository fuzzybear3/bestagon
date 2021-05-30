#https://realpython.com/python-sockets/

# Importing the library
import pygame
from network import Network
from math import *


# Initializing Pygame
pygame.init()

# load and set the logo
logo = pygame.image.load('cat32.png')
pygame.display.set_icon(logo)
pygame.display.set_caption("test program")

# Initializing surface
surface = pygame.display.set_mode((800,600))

# Initialing Color
color = (232,128,173)

def draw_ngon(Surface, color, n, radius, position):
    pi2 = 2 * 3.14

    for i in range(0, n):
        pygame.draw.line(Surface, color, position, (cos(i / n * pi2) * radius + position[0], sin(i / n * pi2) * radius + position[1]))

    return pygame.draw.lines(Surface,
          color,
          True,
          [(cos(i / n * pi2) * radius + position[0], sin(i / n * pi2) * radius + position[1]) for i in range(0, n)])


def read_pos(str):
	str = str.split(",")
	return int(str[0]), int(str[1])


def make_pos(tup):
	return str(tup[0]) + "," + str(tup[1])



running = True
n = Network()


while running:
	# event handling, gets all event from the event queue
	for event in pygame.event.get():
		# only do something if the event is of type QUIT
		if event.type == pygame.QUIT:
			# change the value to False, to exit the main loop
			running = False
			pygame.quit()
	



	
	pygame.event.get()
	mouse = pygame.mouse.get_pressed()
	
	if mouse[0] == True:
		pos = pygame.mouse.get_pos()
		serverData = n.send(make_pos(pos))
		#pygame.draw.rect(surface, color, pygame.Rect(pos[0], pos[1], 5, 5))
		draw_ngon(surface, color, 6, 10, pos)
		for x in serverData:
			draw_ngon(surface, color, 6, 10, x)
		pygame.display.flip()

	elif mouse[1] == True:
		surface.fill((0,0,0))
		pygame.display.flip()
	
	elif mouse[2] == True:
		pos = pygame.mouse.get_pos()
		pygame.draw.rect(surface, (0,0,0), pygame.Rect(pos[0], pos[1], 40, 40))
		pygame.display.flip()

	else:
		serverData = n.send("ping")
		print(serverData)
		for x in serverData:
			draw_ngon(surface, color, 6, 10, x)
		pygame.display.flip()