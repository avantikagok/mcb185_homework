import sys
import mcb185
import gzip
import json

fasta = sys.argv[1]
gff = sys.argv[2]

def print_pwm(pwm, acc, idname, de):
	print('AC', acc)
	print('XX')
	print('ID', idname)
	print('XX')
	print('DE', de)
	print(f'{"PO":<8} {"A":<8} {"C":<8} {"G":<8} {"T":<8} ')
	for i in range(len(pwm)):
		print(f'{i+1:<8} {int(pwm[i]["A"]):<8} {int(pwm[i]["C"]):<8}', end='')
		print(f'{int(pwm[i]["G"]):<8} {int(pwm[i]["T"]):<8}')
	print('XX')
	print('//')


chrom = {}
for defline, seq in mcb185.read_fasta(fasta):
	chid = defline.split()[0]
	chrom[chid] = seq
	
introns = []

with gzip.open(gff, 'rt') as fp:
	for line in fp:
		f = line.split() 
		c = f[0]
		t = f[2]
		b = int(f[3]) - 1
		e = int(f[4]) - 1
		n = f[5]
		s = f[6]
		if n == '.': 
			continue
		n = float(n)
		if t != 'intron': continue
		introns.append((c, b, e, n, s))
		

don = []
for i in range(6):
	don.append({'A': 0, 'C': 0, 'G': 0, 'T': 0})
	
acc = []
for i in range(7):
	acc.append({'A': 0, 'C': 0, 'G': 0, 'T': 0})


for c, b, e, n, s in introns:
	if s == '+':
		iseq = chrom[c][b:e+1]
	else:
		iseq = mcb185.anti_seq(chrom[c][b:e+1])
	dseq = iseq[0:6]
	for i, nt in enumerate(dseq):
		don[i][nt] += 1
	
	aseq = iseq[-7:]
	for i, nt in enumerate(aseq):
		acc[i][nt] += 1

				
print_pwm(acc, 'ag001', 'ACC', 'splice acceptor')
print_pwm(don, 'ag002', 'DON', 'splice donor')
		
		
		
		
		
