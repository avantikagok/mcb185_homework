seq = 'ACGTACGTGGGGGACGTACGTCCCCC'
print(seq)
w = 10

g = seq[0:w].count('G')
c = seq[0:w].count('C')

print(f'0\t{(g + c) / w:.3f}\t{(g - c) / (g + c):.3f}')

for i in range(0, len(seq) - w):
	leavingnt = seq[i]
	newnt = seq[i+w]
	if leavingnt == 'G':
		g -= 1
	elif leavingnt == 'C':
		c -= 1
		
	if newnt == 'G':
		g += 1
	elif newnt == 'C':
		c += 1
		
	if g + c == 0:
		skew = 0
	else:
		skew = (g - c) / (g + c)
	print(f'{i+1}\t{(g + c) / w:.3f}\t{skew:.3f}')
	
