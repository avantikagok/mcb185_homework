import math

def factorial(z):
	if z == 0: return 1
	fac = 1
	for i in range(1, z+1):
		fac = fac * i
	return fac

def poissonprob(k, n):
	prob = ((n ** k) * (math.e ** (-1 * n)) / factorial(k))
	print(prob)
	
poissonprob(15, 3)
poissonprob(4, 4)
poissonprob(234, 237)



#what is the overflow error for the last example?