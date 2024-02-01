def fibonacci():
	f0 = 0
	f1 = 1
	print(f0)
	print(f1)
	count = 1
	for count in range(1, 8):
		fnext = f0 + f1
		print(fnext)
		f0 = f1
		f1 = fnext
		count = count + 1
		
fibonacci()