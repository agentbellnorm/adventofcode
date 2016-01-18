vowels = ["a", "e", "i", "o", "u"]
illegals = ["ab", "cd", "pq", "xy"]
numberOfWords = 0
goodStrings = []
with open("./input.txt") as f:
	while True:
		c = f.readline()
		if not c:
			break
		
		#check three vowels
		enoughVowels = False
		noVowels = 0
		for vow in vowels:
			noVowels += c.count(vow)
			if(noVowels >= 3):
				enoughVowels = True
				break
		
		#check double occurences
		double = False
		prev = ""
		for char in c:
			if(char == prev):
				double = True
				break
			prev = char
		
		#check illegal characters
		illegal = False
		for pair in illegals:
			if pair in c:
				illegal = True
				break

		#determine good or bad
		good = enoughVowels and double and (not illegal)
		if good:
			goodStrings.append(c)

print(len(goodStrings))