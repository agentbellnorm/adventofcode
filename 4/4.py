import hashlib
key = "yzbqklnj"
i = 0
while True:
	saltedKey = key + str(i)
	if(hashlib.md5(saltedKey.encode()).hexdigest()[:5] == "00000"):
		print(i)
		break
	i = i+1
