def nilakanthaseries():
	ninitial = 2
	nmiddle = 3
	nfinal = 4
	total = 0
	for termnumber in range(1, 500):
		if termnumber % 2 == 0:
			sign = -1 
		else:
			sign = 1 
		total = total + sign * (4 / (ninitial * nmiddle * nfinal))
		ninitial = nfinal
		nmiddle = ninitial + 1
		nfinal = ninitial + 2
		termnumber = termnumber + 1
	total = total + 3
	print(total)
	
nilakanthaseries()