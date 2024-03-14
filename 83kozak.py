import sys
import gzip
import dogma
import mcb185


filepath = sys.argv[1]


with gzip.open(filepath, 'rt') as fp:
	number = 0
	coordinates = []
	ntdata = []
	for line in fp:
		number += 1
		line = line.rstrip()
		if 'join' in line: continue
		if 'CDS' in line and '..' in line: 
			firstindex = line.find('(')
			secondindex = line.find(')')
			if 'complement' in line:
				strand = 'negative'
				indexes = line[firstindex + 1: secondindex]
				start, end = indexes.split('..')
				coordinates.append([strand, start, end])
			else:	
				strand = 'positive'
				components = line.split()
				start, end = components[1].split('..')
				coordinates.append([strand, start, end])
		if 'ORIGIN' in line:
			for line in fp:
				miniseq = line.split()
				for i in miniseq[1:]:
					ntdata.append(i)
		sequence = ''.join(ntdata)

reverseseq = mcb185.anti_seq(sequence)

total = 0
kozakntcounts = []
for i in range(0, 14):
	kozakntcounts.append({'a': 0, 'c': 0, 'g': 0, 't': 0})

kozaks = []
for i in coordinates:
	total += 1
	if i[0] == 'positive':
		kozakstart = int(i[1]) - 1 - 9
		kozakend = int(i[2]) - 1 - 9 
		reportstrand = sequence[kozakstart:kozakstart+14]
	if i[0] == 'negative':
		kozakstart = len(reverseseq) - int(i[2]) - 9
		kozakend = len(reverseseq) - int(i[1]) - 1 - 9 
		reportstrand = reverseseq[kozakstart:kozakstart+14]
	kozaks.append(reportstrand)
	


for i in range(len(reportstrand)):
	for kozak in kozaks:
		kozakntcounts[i][kozak[i]] += 1


print('AC IMTSU001')
print('XX')
print('ID ECKOZ')
print('XX')
print('DE: ........')
print(f'{"PO":<8} {"A":<8} {"C":<8} {"G":<8} {"T":<8} ')
for i in range(14):
	print(f'{i+1:<8} {kozakntcounts[i]["a"]:<8}', end='')
	print(f'{kozakntcounts[i]["c"]:<8}', end='')
	print(f'{kozakntcounts[i]["g"]:<8} {kozakntcounts[i]["t"]:<8}')
print('XX')
