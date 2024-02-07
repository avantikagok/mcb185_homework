import random

def dnaseq(number):
	for i in range(1, number):
		print(f'>seq-{i}')
		for i in range(random.randint(50, 60)):
			print(random.choice('ACGT'), end='')
		print()
	
dnaseq(10)