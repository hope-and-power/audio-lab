import pygame as pg, numpy as np
from pygame.locals import *

class Screen:
	# Screen - takes video generator output and displays it on screen
	#	 - also handles screen input and sends it to the Audiolab
	#	Takes:
	#		int (l) - length of screen
	#		int (w) - width of screen
	def __init__(self, l=1024, w=768, dbuff = True):
		pg.init()

		# INITIALIZE SCREEN --------------------------------------------
		size = l,w
		if dbuff:
			screen = pg.display.set_mode((size), DOUBLEBUF)	# manage the screen, doublebuf is a buffer option to allow for smooth animation
			pg.display.flip()
		else:
			screen = pg.display.set_mode((size))	# manage the screen
		# /INITIALIZE SCREEN -------------------------------------------

