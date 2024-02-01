'''i = 1
while i < 10:
	print(i)
	i = i + 3

print('final value of i is', i)



for i in range(5):
	print(i)

print(i)


for char in 'hello':
	print(char)
	
seq = 'GAATTC'
for nt in seq:
	print(nt)
	
for i in range(len(seq)):
	print(seq[i])
	
for nt1 in 'ATGC':
	for nt2 in 'ATGC':
		if nt1 == nt2: print(nt1, nt2, '+1')
		else:		   print(nt1, nt2, '-1')
		
limit = 4
for i in range(0, limit):
	for j in range(i + 1, limit):
		print(i+1, j+1)'''
		
		
		
def triangle(n):
	sum = 0
	for i in range(1, n+1):
		sum = sum + i
	print(sum)
	
triangle(10)