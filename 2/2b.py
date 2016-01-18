rib = 0
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
		biggest = max(sides)
		sides.remove(biggest)
		rib += 2 * sides[0] + 2 * sides[1] + l*h*w



print(rib)