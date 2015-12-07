import mountaincar as mc
import numpy as np
from Tilecoder import numTilings, tilecode, numTiles
from Tilecoder import numTiles as n
from pylab import *  #includes numpy

numRuns = 50
numEpisodes = 200
numActions=3
alpha = 0.5/numTilings
gamma = 1
lmbda = 0.9
Epi = Emu = epsilon = 0
n = numTilings*numTiles*numActions
F = [-1]*np.ones(numTilings)
steps=np.zeros(numEpisodes)
returns=np.zeros(numEpisodes)

runSum = 0.0
for run in xrange(numRuns):
	theta = -0.01*rand(n)
	returnSum = 0.0
	for episodeNum in xrange(numEpisodes):
		G = 0	
#	your code goes here (20-30 lines, depending on modularity)
		step=0
		e=np.zeros(n)
		s=mc.init()
		Q=np.zeros(numActions)
		while s!=None:
			step=step+1
			tilecode(s[0],s[1],F)
			Q=np.zeros(numActions)
			for a in range(3):
				for _ in F:
					Q[a]=Q[a]+theta[_+a*324]
			a=np.argmax(Q)
			r, s1=mc.sample(s,a)
			G+=r
			delta=r-Q[a]
			for i in F:
				e[i+a*324]=1
			if s1==None:
				for i in range(n):
					theta[i]=theta[i]+alpha*delta*e[i]
				break
			tilecode(s1[0],s1[1],F)
			Q=np.zeros(numActions)
			for a in range(3):
				for i in F:
					Q[a]=Q[a]+theta[i+a*324]
			delta=delta+np.max(Q)
			for _ in range(n):
				theta[_]=theta[_]+alpha*delta*e[_]
				e[_]=lmbda*e[_]
			s=s1
		
		print "Episode: ", episodeNum, "Steps:", step, "Return: ", G
		returnSum = returnSum + G
		steps[episodeNum]=steps[episodeNum]+step
		returns[episodeNum]=returns[episodeNum]+G
	print "Average return:", returnSum/numEpisodes
	runSum += returnSum
print "Overall performance: Average sum of return per run:", runSum/numRuns

def Qs(F):
	Q=np.zeros(numActions)
	for a in range(3):
		for _ in F:
			Q[a]=Q[a]+theta[_+a*324]
	return Q

#Additional code here to write average performance data to files for plotting...
#You will first need to add an array in which to collect the data
def writeD():
	f_mean=open('avgret.dat', 'w')
	f_step=open('avgsteps.dat', 'w')
	for _ in range(numEpisodes):
		f_mean.write(repr(_) + ' ' + repr(returns[_]/numRuns))
		f_step.write(repr(_) + ' ' + repr(steps[_]/numRuns))
		f_mean.write('\n')
		f_step.write('\n')
	f_step.close()
	f_mean.close()

def writeF():
	fout = open('value', 'w')
	F = [0]*numTilings
	steps = 50
	for i in range(steps):
		for j in range(steps):
			tilecode(-1.2+i*1.7/steps, -0.07+j*0.14/steps, F)
			height = -max(Qs(F))
			fout.write(repr(height) + ' ')
		fout.write('\n')
	fout.close()

writeF()
writeD()
