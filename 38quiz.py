# Coauthors: Anisha, Varsha, Francesca, Lisa

total = 1
sign = -1
for i in range(3, 10000, 2):
	total = total + sign * (1 / i)
	sign = sign * -1
print("Pi / 4 estimate is", total)
		
