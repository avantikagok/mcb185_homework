import sys
import random

csize = int(sys.argv[1])
rsize = int(sys.argv[2])
rnum = int(sys.argv[3])

chrom = []
for i in range(csize): chrom.append(0)

# fill it up with reads 

for i in range(rnum):
	pos = random.randint(0, csize - rsize)
	for j in range(rsize):
		chrom[pos + j] += 1
		
min = rnum
for n in chrom[rsize:-rsize]:
	if n < min: min = n
print(min)

k = 3
seq = 'ATCTGTGCATCGCTA'
for i in range(0, len(seq) - k + 1, 3):
	win = seq[i:i+k]
	print(win)
	g = win.count('G')
	c = win.count('C')
	print(i, win, (g + c) / k)
		
for i in range(0, csize - rsize + 1):
	print(chrom[i: i + rsize])
	
