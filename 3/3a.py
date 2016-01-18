visited = [(0,0)]
x = 0
y = 0
with open("./input.txt") as f:
	while True:
		c = f.read(1)
		if not c:
			break
		if(c == "^"):
			y = y+1	
		elif(c == ">"):
			x = x+1
		elif(c == "v"):
			y = y-1
		elif(c == "<"):
			x = x-1
		if (x,y) not in visited:
			visited.append((x,y))
print(len(visited))