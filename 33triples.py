def pythagtriples():
	for a in range(1, 101):
		for b in range(1, 101):
			maxvalc = (100**2 + 100**2)**0.5
			c = (a**2 + b**2)**0.5
			if c % 1 == 0:
				print(a, b, c)
	
pythagtriples()

