#https://realpython.com/python-sockets/

# Importing the library
import pygame
from network import Network
from math import *
from Player import Player


#Settings
CIRCLE_SIZE = 8

# Initializing Pygame
pygame.init()

# load and set the logo
logo = pygame.image.load('cat32.png')
pygame.display.set_icon(logo)
pygame.display.set_caption("test program")

# Initializing surface
surface = pygame.display.set_mode((800,600))

# Initialing Color
#color = (232,128,173)
#color = (24,60,200)


def draw_ngon(Surface, color, n, radius, position):
    pi2 = 2 * 3.14

    for i in range(0, n):
        pygame.draw.line(Surface, color, position, (cos(i / n * pi2) * radius + position[0], sin(i / n * pi2) * radius + position[1]))

    return pygame.draw.lines(Surface,
          color,
          True,
          [(cos(i / n * pi2) * radius + position[0], sin(i / n * pi2) * radius + position[1]) for i in range(0, n)])



running = True
n = Network()
P = n.getP()

clock = pygame.time.Clock()
#print(P)

while running:

	clock.tick(400)
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
		P.pos = pygame.mouse.get_pos()
		players = n.send(P)
		#pygame.draw.rect(surface, color, pygame.Rect(pos[0], pos[1], 5, 5))
		#draw_ngon(surface, P.color, 6, 10, P.pos)
		pygame.draw.circle(surface, P.color, P.pos, CIRCLE_SIZE)
		for x in players:
			#draw_ngon(surface, x.color, 6, 10, x.pos)
			pygame.draw.circle(surface, x.color, x.pos, CIRCLE_SIZE)
		pygame.display.flip()

	elif mouse[1] == True:
		surface.fill((0,0,0))
		pygame.display.flip()
	
	elif mouse[2] == True:
		pos = pygame.mouse.get_pos()
		pygame.draw.rect(surface, (0,0,0), pygame.Rect(pos[0], pos[1], 40, 40))
		pygame.display.flip()

	else:
		players = n.Ping_get_data("ping")
		#print(players)
		for x in players:
			#draw_ngon(surface, x.color, 6, 10, x.pos)
			pygame.draw.circle(surface, x.color, x.pos, CIRCLE_SIZE)
		pygame.display.flip()