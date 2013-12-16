# each bucket has an angle, a volume of water, a maximum volume, a hole size (aka water loss rate)
# bucket = list of (theta, vol)
# ALL IN 2D
from numpy import pi, sin
gravity = 9.8		# m/s^2
dt = 0.1		# second
bucket_width = 0.2	# meters
bucket_height = 0.1	# meters
bucket_vol = bucket_height*bucket_width	# m^2
hole_width = 0.05	# meters
num_buckets = 6
pipe_flow = 2/60	# m^2 per second
wheel_radius = 1	# meter
pipe_width = 0.2	# meters
pipe_x = 1		# center of pipe is located at the right end of the wheel
buckets = []

for i in range(num_buckets):	# initialize bucket and water heights
	theta = (2*pi)/num_buckets*i
	buckets.append((theta,0))

def addwater(dt)
	a = pipe_x - pipe_width/2
	b = pipe_x + pipe_width/2
	for bu in buckets:
		theta = bu[0]
		c = wheel_radius * sin(theta) - bucket_width/2	# [c,d] is the x-interval of the bucket
		d = wheel_radius * sin(theta) + bucket_width/2
		# calculate overlap
		if a < c < b:
			if d < b:
				overlap = d - c	# whole overlap
			else:
				overlap = b - c	# left side of bucket and right side of pipe overlap
		else if a < d < b:
			if c > a:
				overlap = d - c	# whole overlap
			else:
				overlap = d - a # right side of bucket and left side of pipe overlap
		else:
			overlap = 0
		# TODO calculate water gain
		if b[1] < bucket_height:
			newHeight = b[1] 


def losewater(dt)
	for bu in buckets:
		newHeight = bu[1] - (hole_area*(2*bu[1]*gravity)**0.5)*dt/bucket_base	# orig water height - dv/dt*dt/bucket_base
		if newHeight >=0:
			bu[1] = newHeight
		else:
			bu[1] = 0

def d2thetadt2()

	
