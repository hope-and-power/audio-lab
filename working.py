# Generates fractals with a GUI

import numpy as np
import matplotlib.pyplot as plt
import Tkinter as tk
import cv2, time
#----------------------------------------------------------------------------------------#		   	
resX, resY = 300, 300 			# resolution
lowX, highX, lowY, highY = -1, 1, -1, 1	# size of complex domain
nIt = 9					# how many times to iterate the Z-function
Z = lambda z: z*(z-1)			# our iterated Z-function TODO make a string input for GUI -> Z

z = np.empty(shape=(resX,resY), dtype=complex)	# initialize pointset matrix
for y in range(resY):			# loop over all relevant x,y
	for x in range(resX):
		yval = (float(y)/resY) * (highY-lowY) + lowY
		xval = (float(x)/resX) * (highX-lowX) + lowX
		z[x,y] = complex(xval,yval)

s = time.time()			  	# start timer			
z = Z(z) for i in range(nIt)		# apply function nIt times
print time.time() - s			# how long did that take?
r = np.abs(z) 

hsv = np.concatenate(((np.angle(z) + np.pi/2)[:,:,None],		# hue
					  np.exp(-r)[:,:,None],	# saturation
					  np.exp(-r)[:,:,None]),2)		# value
hsv = np.uint8(hsv * 255)					  
rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR) 
print time.time() - s
plt.imshow(rgb)
plt.show()


#----------------------------------------------------------------------------------------#
class Slider(tk.Canvas):
	def __init__(self,parent,text):
		self.HEIGHT = parent.SLIDERHEIGHT
		self.THICKNESS = 3
		self.POINTERSIZE = 9
		self.OFFSETX = 80
		self.text = text
		tk.Canvas.__init__(self,parent,height=self.HEIGHT,
						   background='black', highlightthickness=0)
		self.parent = parent
		self.level = .5
		self.drag_data = {'x':None, 'y':None}	
		self.bind('<ButtonPress-1>', self.my_click)
		self.bind('<ButtonRelease-1>', self.my_release)
		self.bind('<B1-Motion>', self.my_motion)
		
		self.line = self.create_rectangle(self.OFFSETX, self.HEIGHT/3,
							  		350, self.HEIGHT/3 + self.THICKNESS, 
							  		fill='gray')
		self.pointer = self.create_polygon(0,0,0,0,0,0, fill='gray')
		self.reposition()
		
		self.label = tk.Label(self, text=self.text, fg='white', bg='black')
		self.label.pack(side='left')
		
	def reposition(self):
		dims = (self.level*(330-self.OFFSETX) + self.OFFSETX + 10,
				self.HEIGHT/3 + self.THICKNESS/2 - self.POINTERSIZE,
				self.level*(330-self.OFFSETX) + self.OFFSETX + 10,
				self.HEIGHT/3 + self.THICKNESS/2 + self.POINTERSIZE,
				self.level*(330-self.OFFSETX) + self.OFFSETX + 2*self.POINTERSIZE + 10,
				self.HEIGHT/3 + self.THICKNESS/2)
		self.coords(self.pointer,dims)				
		
	def my_click(self,event):
		if (event.x > self.level*(330-self.OFFSETX) + self.OFFSETX 					and
			event.x < self.level*(330-self.OFFSETX) + self.OFFSETX + 2*self.POINTERSIZE + 20 and
			event.y > self.HEIGHT/3 + self.THICKNESS/2 - self.POINTERSIZE - 5       and
			event.y < self.HEIGHT/3 + self.THICKNESS/2 + self.POINTERSIZE + 5):
			self.drag_data = event.x
	def my_release(self,event):
		self.drag_data = None
	def my_motion(self,event):
		if self.drag_data != None:
			self.level += float(event.x - self.drag_data)/(330-self.OFFSETX)
			self.level = np.minimum(np.maximum(self.level,0),1)
			self.reposition()
			self.drag_data = event.x
			
#----------------------------------------------------------------------------------------#		   	
