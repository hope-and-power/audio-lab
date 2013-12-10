#----------------------------------------------------------------------------------------#		
# These functions return dictionaries with arrays of frequencies (samples)
# 	- they return samples that are precisely tmeas long
#----------------------------------------------------------------------------------------#		
import math, wave, aifc, array, os, numpy as np
import struct
fs = 44100 # sampling rate
#----------------------------------------------------------------------------------------#		
def sine(tmeas):
	sound_ref = {}
	for i in range(1,89):
		new_wave = []
		freq = 2 ** (float(i-49)/12) * 440
		period = [np.sin(freq * t * 2 * np.pi / fs) for t in xrange(int(fs/freq))]
		period = [int(2**14 * x) for x in period]
		while len(new_wave) < fs * tmeas: new_wave += period
		sound_ref.update({i:new_wave})
	return sound_ref	
#----------------------------------------------------------------------------------------#		
def piano(tmeas):
	sound_ref = {}
	for i in range(1,89):	
		f = wave.open('audio/piano_sounds/' + repr(i) + '.wav')		# open audio file
		str, new_frame = '', f.readframes(1)						# read file to string
		while new_frame != '': 
			str += new_frame
			new_frame = f.readframes(fs)	
		ar = array.array('h', str)					# convert string to int array
		sound_ref.update({i : np.array(ar[:tmeas * fs], np.int32)})
	return sound_ref
#----------------------------------------------------------------------------------------#		
