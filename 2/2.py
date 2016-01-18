area = 0
with open("./input.txt") as f:
	while True:
		c = f.readline()
		if not c:
			break
		sides = c.split("x")
		sides = list(map(int, sides))
		l = sides[0]
		w = sides[1]
		h = sides[2]
		area += (2*l*w) + (2*w*h) + (2*l*h) + min(l*w, w*h, l*h)

print(area)
