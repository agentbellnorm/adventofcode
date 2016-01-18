i = 0
char = 1
with open("./input.txt") as f:
	while True:
		c = f.read(1)
		if not c:
			break
		elif(c == "("):
			i = i + 1
		elif(c == ")"):
			i = i - 1
		if(i == -1):
			print(char)
			break
		char = char + 1