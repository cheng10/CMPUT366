numTilings = 4
numTiles=81
	
def tilecode(p,v,tileIndices):
	# write your tilecoder here (5 lines or so)
	for i in range (numTilings):
		p_axis=int(((p+1.2)+i*0.2125/numTilings)*8/1.7)
		v_axis=int(((v+0.07)+i*0.0175/numTilings)*8/0.14)
		tileIndices[i]=p_axis+9*v_axis+i*numTiles
