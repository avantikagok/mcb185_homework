import sys
import mcb185
import itertools


def generatekcountdict(k):
	kcount = {}
	for nts in itertools.product('ACGT', repeat=k):
		kmer = ''.join(nts)
		kcount[kmer] = 0
	return kcount
		

def hasmissingkmer(kcount, sequence, k):
	zerokmers = []
	foundzero = False
	for i in range(len(sequence) - k + 1):
		kmer = sequence[i:i+k]
		kcount[kmer] += 1
	reverse = mcb185.anti_seq(sequence)
	for i in range(len(reverse) - k + 1):
		kmer = reverse[i:i+k]
		kcount[kmer] += 1
	#print(kcount)
	for kmer in kcount:
		if kcount[kmer] == 0:
			zerokmers.append(kmer)
			foundzero = True
	if foundzero == True:
		print(zerokmers, len(zerokmers))
		return True
	else:
		return False


for defline, seq in mcb185.read_fasta(sys.argv[1]):
	for k in range(len(seq)):
		currentdict = generatekcountdict(k)
		if hasmissingkmer(currentdict, seq, k):
			print('Found missing kmers at kmer length', k)
			break
		
	
	