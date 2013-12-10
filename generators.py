#----------------------------------------------------------------------------------------#		
import numpy as np
#----------------------------------------------------------------------------------------#
#------------------ All the classes below should have next_note() method ----------------#	i.e. they are subclasses of the Generator class
#----------------------------------------------------------------------------------------#	TODO: create Generator class
class Markov:
	def __init__(self,song,order):
		self.ord = order									# order of markov model
		self.song = song									# sequence used for training
		
		self.n2i = dict({note:i for i,note in enumerate(set(song))})     # note to index
		self.i2n = dict({self.n2i[note]:note for note in set(song)})	 # index to note
		
		self.M = self.transition_matrix()  # this matrix counts every prefix-note combo
		self.hist = tuple([self.n2i[n] for n in self.song[-self.ord:]])  # preset hist to 
																	    # end of the song	
	def transition_matrix(self):
		M = np.zeros((len(set(self.song)),)*(self.ord+1))	# initialize to array of zeros
		song = self.song + self.song[:self.ord]		# augment song so to mimic wrapping TODO: this is no good - we should incorporate pauses a the end of phrases and songs
		for i in range(len(self.song)):				# for every n-gram in song, add 1 to M
			M[tuple([self.n2i[n] for n in song[i:i+self.ord+1]])] += 1 
		return M
		
	def sample(self,dist): 					# return samples from categorical distribution
		dist = dist / (np.sum(dist) + .001) # by using sequence of probabilities to define to define series of thresholds in interval.
		dist = dist.flatten()				# get val by drawing sample uniformly from 0
		threshes = [dist[0]]      			# 1 and returning index of smallest threshold
		for d in dist[1:]: threshes.append(threshes[-1] + d)      # that is  > the sample
		x = np.random.uniform(0,np.max(threshes))
		return [x < t for t in threshes].index(True)
		
	def next_note(self):
		hist_coord = self.hist + (None,)			# draws from the markov chain
		note = self.sample(self.M[hist_coord])
		self.hist = self.hist[1:] + (note,)			# update history for each new draw
		return  self.i2n[note]
#----------------------------------------------------------------------------------------#		
class Loop:
	def __init__(self,song):
		self.song = song
		self.tracker = 0
		
	def next_note(self):
		self.tracker += 1
		return self.song[self.tracker % len(self.song)]		
#----------------------------------------------------------------------------------------#		
