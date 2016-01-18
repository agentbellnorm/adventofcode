#init (Don't print matrix!)
lights = []
lit = 0
for i in range(1000):
	lights.append([])
	for j in range(1000):
		lights[i].append('turn off')
print("initiated")

def alterState(x1, y1, x2, y2, instruct):
	for i in range(x1, x2+1):
		for j in range(y1, y2+1):		
			if(instruct == 'toggle'):
				if(lights[i][j] == 'turn on'):
					lights[i][j] = 'turn off'
				elif(lights[i][j] == 'turn off'):
					lights[i][j] = 'turn on'
			else:
				lights[i][j] = instruct

#alterState(0,999,0,999,'turn on')
def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
count = 0
with open("./input.txt") as f:
	#for each line
	while True:
		c = f.readline()
		if not c:
			print("#"+str(count)+" - end of file")
			break
		c = c.strip()
		#get instruction
		for i in range(len(c)):
			if(RepresentsInt(c[i])):
				coordsInfo = c[i:len(c)-1]
				instruct = c[:i-1].strip()
				break
		coordsInfo = coordsInfo.split(" through ")
		coordsInfo[0] = coordsInfo[0].split(',')
		coordsInfo[1] = coordsInfo[1].split(',')
		alterState(int(coordsInfo[0][0]), int(coordsInfo[0][1]) +1, int(coordsInfo[1][0]), int(coordsInfo[1][1]) +1, instruct)
		count = count+1
print(sum(list(map(lambda x: x.count('turn on'), lights))))
