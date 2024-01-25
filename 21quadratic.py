import math 
import sys
def quadratic (a, b, c):
	if b**2 - 4*a*c < 0:
		return None, None, ": No real solutions"
	elif b**2 - 4*a*c == 0:
		x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
		return x1, None, ": One real solution"
	else:
		x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
		x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
		return x1, x2, ": Two real solutions"



x1, x2, solnum = quadratic (5, -7, 14)
print (x1, x2, solnum)

x1, x2, solnum = quadratic (1, -7, -3)
print (x1, x2, solnum)

x1, x2, solnum = quadratic (1, 2, 1)
print (x1, x2, solnum)

