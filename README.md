audio-lab
=========

Algorithmic music generation

To use, for example:
	>>> import sound
	>>> import generators
	>>> import songs
	>>> import sounds
	>>> import audiolab

	# EXAMPLE CODE 1  (play randomized version of twinkle twinkle w/ piano key sounds)
	>>> measure_duration = 3
	>>> my_bbox = audiolab.BoomBox(tmeas=measure_duration)
	>>> my_voice = audiolab.Voice(my_bbox)
	>>> my_voice.sound_ref = sounds.piano(measure_duration)
	>>> my_voice.note_gen = generators.Markov(songs.twinkle_twinkle(),2)
	>>> my_bbox.play()

	# EXAMPLE CODE 2 (play prime numbers using sine tones on an endless loop)

	>>> measure_duration = 2
	>>> my_bbox = audiolab.BoomBox(tmeas=measure_duration)
	>>> my_voice =audiolab. Voice(my_bbox)
	>>> my_voice.sound_ref = sounds.sine(measure_duration)
	>>> my_voice.note_gen = generators.Loop(songs.prime_song())
	>>> my_bbox.play()
