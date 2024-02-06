# Coauthors: Anisha, Varsha, Francesca, Lisa

'''total = 1
sign = -1
for i in range(3, 10000, 2):
	total = total + sign * (1 / i)
	sign = sign * -1
print("Pi / 4 estimate is", total)
		
'''
def nilakanthaseries(limit):
	ninitial = 2
	nmiddle = 3
	nfinal = 4
	ntotal = 3
	termnumber = 1
	for termnumber in range(1, limit + 1):
		if termnumber % 2 == 0:
			sign = -1 
		else:
			sign = 1 
		ntotal = ntotal + sign * (4 / (ninitial * nmiddle * nfinal))
		ninitial = nfinal
		nmiddle = ninitial + 1
		nfinal = ninitial + 2
		termnumber = termnumber + 1
	return(ntotal)


def gregleib(limit):
	total = 1
	sign = -1
	i = 3
	realpi = 0
	for i in range(3, limit, 2):
		total = total + sign * (1 / i)
		sign = sign * -1
		realpi = total * 4
	return(realpi)
	


for i in range(1,101):
	print(nilakanthaseries(i), gregleib(i))