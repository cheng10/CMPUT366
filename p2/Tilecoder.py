numTilings = 8
	
def tilecode(x,y,tileIndices):
	# write your tilecoder here (5 lines or so)
	for i in range (0,numTilings):
		x_axis=int((x+i*0.6/numTilings)*10/6)
		y_axis=int((y+i*0.6/numTilings)*10/6)
		tileIndices[i]=x_axis+11*y_axis+i*121
		
def printTileCoderIndices(x,y):
	tileIndices = [-1]*numTilings
	tilecode(x,y,tileIndices)
	print 'Tile indices for input (',x,',',y,') are : ', tileIndices

#printTileCoderIndices(0.1,0.1)
#printTileCoderIndices(4.0,2.0)
#printTileCoderIndices(5.99,5.99)
#printTileCoderIndices(4.0,2.1)
