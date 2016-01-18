goodStrings = []
with open("./input.txt") as f:
	#for each line
	while True:
		c = f.readline()
		if not c:
			break

		#check double occurences of pairs
		doublepair = False
		for i in range(14):
			pair = c[i:i+2]
			if(c.count(pair) >= 2):
				doublepair = True
				print("pair: " + pair + " " + c)
				break

		#check for pattern 'a*a'
		nextrepeat = False
		for i in range(14):
			if(c[i] == c[i+2]):
				nextrepeat = True
				print("pattern: "+c[i] + "*" + c[i] + " " + c)
				break

		#determine good or bad
		good = doublepair and nextrepeat
		if good:
			goodStrings.append(c)

print(len(goodStrings))