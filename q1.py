def isUnique(string):
	uchars=[]
	for c in string:
		if c in uchars:
			return False
		else:
			uchars.append(c)
	return True
