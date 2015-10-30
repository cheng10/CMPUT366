import blackjack
import numpy as np
from pylab import *

numEpisodes = 2000
returnSum = 0.0

for episodeNum in range(numEpisodes):
	s = blackjack.init()
	while s!=-1:
		a = np.random.randint(0,2)
		G,s_=blackjack.sample(s,a)
		s=s_
	print "Episode: ", episodeNum, "Return: ", G
	returnSum = returnSum + G
print "Average return: ", returnSum/numEpisodes
