def factorial(z):
	if z == 0: return 1
	fac = 1
	for i in range(1, z+1):
		fac = fac * i
	return fac
		

def nchoosek(n, k):
	assert n >= k
	ans = factorial(n) / (factorial(k) * factorial(n - k))
	print(n, "choose", k, "is", ans)


nchoosek(10, 4)
nchoosek(28, 6)
nchoosek(50, 46)