import gzip
import sys
import json
import mcb185


#refcds = []

fas = sys.argv[1]	
orflen = sys.argv[2]


#reference coordinates to compare with
refcds = []
with gzip.open(sys.argv[3], 'rt') as fp:
	for line in fp:
		if line.startswith('#'): continue
		f = line.split()
		if f[2] != 'CDS': continue
		chrom = f[0]
		beg = int(f[3]) - 1
		end = int(f[4]) - 1
		s = f[6]
		#n = int(f[5])
		if end - beg >= 300:
			refcds.append({
			'chrom': chrom,
			'beg': beg,
			'end': end,
			'strand': s})
#print(refcds)


		
def findcds(seq, minlength, strand):
	startend = []
	start = 'ATG'
	stop = ['TAA', 'TGA', 'TAG']
	#stopused = {}
	
	for frame in range(3):
		currentseq = seq[frame:]
		startindex = 0
		while startindex < len(seq) - int(minlength):
			if currentseq[startindex:startindex+3] != 'ATG':
				startindex += 3
				continue	
				
			for endindex in range(startindex + 3, len(seq), 3):
				codon = currentseq[endindex:endindex+3]
				if codon in stop:
					break	
			orflength = endindex - startindex + 1
			
			if orflength > int(minlength):
						#if j in stopused: continue
						if strand == 'positive':
							startend.append([startindex + frame, endindex + frame + 3 - 1])
	
						if strand == 'negative':
							newstart = len(seq) - (endindex + frame + 3) 
							newend = len(seq) - startindex + frame - 1
							startend.append([newstart, newend])
			startindex = endindex 
			
	return startend
		
'''
	while startindex < len(seq) - int(minlength):
		if seq[startindex:startindex+3] != 'ATG':
			startindex += 3
			continue
		for endindex in range(startindex + 3, len(seq), 3):
			codon = seq[endindex:endindex+3]
			if codon in stop:
				break
		orflength = endindex - startindex + 1
		if seq[i:i+3] == start:
			for j in range(i+3, len(seq) - int(minlength), 3):
				if seq[j:j+3] in stop:
					orflength = j + 3 - i
					if orflength > int(minlength):
						#if j in stopused: continue
						if strand == 'positive':
							startend.append([i, j + 3 - 1])
							i = j + 3
							break	
						if strand == 'negative':
							newstart = len(seq) - (j + 3) 
							newend = len(seq) - i - 1
							startend.append([newstart, newend])
							i + j + 3
							break	
					else:
						i += 3
	#startend = startend.sort()
	print(len(startend))
	return startend


'''

def output(indexes, defline, strand):
	for start, end in indexes:
		print(f"{defline}\t.\tCDS\t{start}\t{end}\t.\t{strand}\t.\t.")
	


for defline, seq in mcb185.read_fasta(fas):
	positiveorfs = findcds(seq, orflen, 'positive')
	output(positiveorfs, defline, 'positive')
	negstrand = mcb185.anti_seq(seq)
	negativeorfs = findcds(negstrand, orflen, 'negative')
	output(negativeorfs, defline, 'negative')
	

#print(len(seq))
#print(len(negstrand))
	
	
	
	

	
	
	
	
	
	
	
	


		

