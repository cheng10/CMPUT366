import blackjack as bj
import numpy as np
import math
from pylab import *

numEpisodes =int(math.pow(10,6))
returnSum = 0.0
emu=0.01
epi=0.01
alpha=0.001
num_states=182
num_actions=2
Q=0.00001*np.random.random((num_states,num_actions))
Q[-1,0]=Q[-1,1]=0

def rand_policy(state):
	global returnSum
	s=state
	while s!=-1:
		a=np.random.randint(0,2)
		r,s_=bj.sample(s,a)
		Q[s,a]=Q[s,a]+alpha*(r+0.5*Q[s_,0]+0.5*Q[s_,1]-Q[s,a])
		s=s_
	returnSum=returnSum + r

def exp_sarsa(state):
	global returnSum
	s=state
	while s!=-1:
		if Q[s,0]>Q[s,1]:
			a=0
		else:
			a=1
		r,s_=bj.sample(s,a)
# a_ is the actin choosen by target epsilon greedy policy
		rand=np.random.random()
		if rand<epi:
#		rand
			a_=np.random.randint(0,2)
		else:
#		greedy
			a_=np.argmax(Q[s_])
		Q[s,a]=Q[s,a]+alpha*(r+Q[s_,a_]-Q[s,a])
		s=s_
	returnSum=returnSum + r

def sarsa_policy(state):
	if Q[state,0]>Q[state,1]:
		return 0
	else:
		return 1

def deter_policy(state):
	global returnSum
	s=state
	while s!=-1:
		r,s_=bj.sample(s,sarsa_policy(s))
		s=s_
	returnSum=returnSum + r

#main function
#policy learning
for _ in range(numEpisodes):
	if _%10000==0:
		print "Episode:",_
		print "Average return:",returnSum/(_+1)
	s=bj.init()
	rand=np.random.random()
	if rand<emu:
#		print "rand:",rand,"policy: rand"
		rand_policy(s)
	else:
		exp_sarsa(s)
#		print "rand:",rand,"policy: ExpectedSarsa"

bj.printPolicy(sarsa_policy)
print "Average return:",returnSum/numEpisodes

#determinstic policy
returnSum=0.0
numEpisodes=int(math.pow(10,7))
for _ in range(numEpisodes):
	if _%10000==0:
		print "Episode:",_
		print "Average return:",returnSum/(_+1)
	s=bj.init()
	deter_policy(s)
bj.printPolicy(sarsa_policy)
print "Average return:",returnSum/numEpisodes
print "alpha, emu, epi, episodes:",alpha,emu,epi,numEpisodes
