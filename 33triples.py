def pythagtriples(limit):
	for a in range(1, limit + 1):
		for b in range(a + 1, limit + 1):
			c = (a**2 + b**2)**0.5
			if c % 1 == 0:
				print(a, b, c)
	
pythagtriples(99)


