import random

insidecircle = 0
totalcount = 0

while True:
	x = random.random()
	y = random.random()
	totalcount += 1
	distance = (x ** 2 + y ** 2) ** 0.5
	if distance < 1:
		insidecircle += 1
	piapprox = (insidecircle / totalcount) * 4
	print(piapprox) 