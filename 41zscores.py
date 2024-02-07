import random

def zscore(val):
	z = val - 0 / 1
	return val

z1 = 0
z2 = 0
z3 = 0

totalcount = 22030
for i in range (totalcount):
	val = random.gauss(0.0, 1.0)
	if abs(zscore(val)) <= 1:
		z1 = z1 + 1
	if abs(zscore(val)) <= 2:
		z2 = z2 + 1
	if abs(zscore(val)) <= 3:
		z3 = z3 + 1
print(z1 / totalcount , z2 / totalcount, z3 / totalcount)
	
	
print('a\tb\tcat\tdogma')
print(10, 20, 30, 40, sep='\t')

i = 1
pi = 3.14
print('normal string {i} {pi}')
print(f'formatted string {i} {pi}')
print(f'tau {pi + pi}')

print(f'formatted string {i} {pi:.3f}')

import sys
print('logging', file=sys.stderr)

random.seed(1)
print(random.random())
print(random.random())
random.seed(2)
print(random.random())
print(random.random())
random.seed(1)
print(random.random())
print(random.random())
