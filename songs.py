#----------------------------------------------------------------------------------------#		
def twinkle_twinkle(): 
	return [		
	((28,),8), ((28,),8), ((35,),8), ((35,),8), ((37,),8), ((37,),8), ((35,),8), ((),8), 
	((33,),8), ((33,),8), ((32,),8), ((32,),8), ((30,),8), ((30,),8), ((28,),8), ((),8),
    ((35,),8), ((35,),8), ((33,),8), ((33,),8), ((32,),8), ((32,),8), ((30,),8), ((),8),
	((35,),8), ((35,),8), ((33,),8), ((33,),8), ((32,),8), ((32,),8), ((30,),8), ((),8),
	((28,),8), ((28,),8), ((35,),8), ((35,),8), ((37,),8), ((37,),8), ((35,),8), ((),8),
	((33,),8), ((33,),8), ((32,),8), ((32,),8), ((30,),8), ((30,),8), ((28,),8), ((),8)]
#----------------------------------------------------------------------------------------#		
def prime_song(): 
	notes = []
	primes = [2]
	for i in range(3,10000):
		if not 0 in [i % p for p in primes]:
			primes.append(i)
			notes.append(((i % 24 + 36,),8))
	return notes
#----------------------------------------------------------------------------------------#		