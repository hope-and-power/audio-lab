# Clock keeps track of time and communicates sounds generated from children (generators) to peers (boombox, screen)
# 	takes integers from generators
#	sends sound arrays to the boombox and 3D arrays to screen (x,y,RGB)
import time

class Clk:
	def __init__(self, beats = 4):
		self.start = time.time()	# time as a float in seconds
		self.beat = beats # per measure

	def time():
		return time.time() - self.start

	def beat()
		return int(time.time()%beats)
	

