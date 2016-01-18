visited = [(0,0)]
i = 0
sx = 0
sy = 0
rx = 0
ry = 0
with open("./input.txt") as f:
	while True:
		c = f.read(1)
		if not c:
			break
		if(i%2 == 0):
			if(c == "^"):
				sy = sy+1	
			elif(c == ">"):
				sx = sx+1
			elif(c == "v"):
				sy = sy-1
			elif(c == "<"):
				sx = sx-1
			if (sx,sy) not in visited:
				visited.append((sx,sy))
		else:
			if(c == "^"):
				ry = ry+1	
			elif(c == ">"):
				rx = rx+1
			elif(c == "v"):
				ry = ry-1
			elif(c == "<"):
				rx = rx-1
			if (rx,ry) not in visited:
				visited.append((rx,ry))
		i = i+1
print(len(visited))