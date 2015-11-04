import blackjack as bj
import numpy as np
from pylab import *

numEpisodes = 1000000
returnSum = 0.0

num_states = 181
num_actions = 2

alpha = 0.001

e_behavior = 0.01
e_target= 0.01

def actionProb(e,a,s):
    if np.argmax(Q[s]) == a:
        return 1 - e + e/num_actions
    else:
        return e/num_actions


Q =  0.00001*np.random.rand(num_states,num_actions)

for episodeNum in range(numEpisodes):
    G = 0

    s = bj.init()
    while s != -1:
        a = np.random.choice(2, p=[actionProb(e_behavior,0,s),actionProb(e_behavior,1,s)])
        r, s1 = bj.sample(s,a)
        Q[s,a] = Q[s,a] + alpha*(r + actionProb(e_target,0,s1)*Q[s1,0] + actionProb(e_target,1,s1)*Q[s1,1] - Q[s,a])
        s = s1
        G+=r

    returnSum = returnSum + G

    if episodeNum%10000 == 0:
        print "Episode: ", episodeNum
        print "Average return: ", returnSum/(episodeNum+1)
    
def learnedPolicy(s):
    return np.argmax(Q[s])

bj.printPolicy(learnedPolicy)

returnSum = 0.0

for episodeNum in range(numEpisodes):
    G = 0

    s = bj.init()
    while s != -1:
        r, s = bj.sample(s,learnedPolicy(s))
        G+=r

    returnSum = returnSum + G

    if episodeNum%10000 == 0:
        print "Episode: ", episodeNum
        print "Average return: ", returnSum/(episodeNum+1)