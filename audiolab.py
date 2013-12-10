#----------------------------------------------------------------------------------------#		
import pyaudio, struct, numpy as np, scipy.ndimage as sn
fs = 44100		   # sampling rate

import sounds	   # contains dictionaries which map notes (represented as ints) to sounds				  
import generators  # contains classes which generate notes (most init with song as input)
import songs	   # contains songs, represented as lists of notes, where a note is a 
				   # tuple, ( (<note1>,<note2>,...), <note_length> ), where the outputed
				   # length is tmeas/note_length. rests are written ( (), <rest_length> )
#----------------------------------------------------------------------------------------#		
class BoomBox:
	def __init__(self, tmeas=2, tsteps=32):
		self.tmeas = tmeas  					 # length of measure in seconds
		self.tsteps = tsteps 					 # number of time steps in measure
		self.dt = tmeas * fs / tsteps			# change in time between each sampled frequency
		self.last_sound = np.zeros(self.dt * fs) # keep track of last sound to form smooth
												 # transitions between sound chunks
		self.STREAMING = False					 # bool: whether sound is being made
		self.voices = []						 # list of instances of class: Voice
		
	def play(self):
		self.STREAMING = True	
		p = pyaudio.PyAudio()			
		self.stream = p.open(format=8, channels=1, rate=fs, output=True)
		while self.STREAMING: self.stream.write(self.get_next_sound())
		
	def get_next_sound(self):
		sound_bytes = [v.next_sound() for v in self.voices]	# An array of sampled frequencies from the constituent voices
		sound_bytes = [sound for sound in sound_bytes if sound != None]
		output = np.zeros(self.dt)
		for sound in sound_bytes: output += sound / len(sound_bytes)	# Sum the sound_bytes scaled down by the number of sound_bytes (= number of voices) This adds arrays piecewise to arrays
		return ''.join(struct.pack('h', int(samp)) for samp in output)	# pack the samples in output together
		
#----------------------------------------------------------------------------------------#		
class Voice:
	def __init__(self,parent):
		self.parent = parent	# Boombox is parent class
		parent.voices.append(self)
	
		self.sound_ref = None
		self.note_gen = None
		self.sound_queue = []
	
	def new_sound(self):
		n = self.note_gen.next_note()	# notes
		s = [self.sound_ref[x] for x in n[0]]	# sounds for those notes
		a = np.zeros(self.parent.tmeas * fs / n[1])	# container for the samples 
		for x in s: a += np.array(x[:self.parent.tmeas * fs / n[1]]) / len(s)
		# apply modifications to a
		#a = self.phase_align(a,1000)
		# done modifying
		for i in range(self.parent.tsteps / n[1]):
			self.sound_queue.insert(0,a[i*self.parent.dt:(i+1)*self.parent.dt])
			
	def next_sound(self):	
		if len(self.sound_queue) == 0: self.new_sound() 
		return self.sound_queue.pop()
		
	def phase_align(self,clip,pad):     # this method ensures each clip starts and ends
		def align_front(clip):			# with 0 to avoid discontinuous transitions
			first0 = np.min(np.nonzero(np.abs(clip[:pad]) < 20)[0])
			clip[:pad] = np.interp(np.linspace(0, pad-first0, num=pad), 
								   np.arange(pad-first0),clip[first0:pad])
			return clip
		clip = align_front(clip)
		return align_front(clip[::-1])[::-1]
#----------------------------------------------------------------------------------------#		
