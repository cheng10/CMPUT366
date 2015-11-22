numTilings = 8
    
def tilecode(x,y,tileIndices):
    # write your tilecoder here (5 lines or so)
    i = 0
    for i in range (0,numTilings):
        tileIndices[i] = int((x+i*0.6/8)*10/6)+11*int((y+i*0.6/8)*10/6) + i * 121
        
def printTileCoderIndices(x,y):
    tileIndices = [-1]*numTilings
    tilecode(x,y,tileIndices)
    
    print 'Tile indices for input (',x,',',y,') are : ', tileIndices

printTileCoderIndices(0.1,0.1)
printTileCoderIndices(4.0,2.0)
printTileCoderIndices(5.99,5.99)
printTileCoderIndices(4.0,2.1)
    
# Why?
# Ans 1: Because each map has 121 tiles, and the tile counting starts from 0, So
# the first tiling runs from 0 to 120, and the scond will continue from 121 to 241
# 
# Ans 2: Because if we map the input coordinates to the tilings, 
# on the first tiling, it will be in the first tile, which is 0. Then 
# on the second tiling, will be 0 + 121, which is 121, etc
#
# Ans 3: As the input space shift, the coordinates will shift too, so it can shift 
# to another tile.
#
# Ans 4. It shift 8 times, so total there are 8 * 121, which is 968 tiles,
# and if count from zero, the largest index would be 967.