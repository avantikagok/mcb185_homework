import gzip
"""
path = '../MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz'
with gzip.open(path, 'rt') as fp:
	for line in fp:
		if line[0] == '#': continue
		words = line.split()
		if words[2] != 'CDS': continue
		beg = int(words[3])
		end = int(words[4])
		print(end - beg + 1)
		

lengths = []
path = '../MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz'
with gzip.open(path, 'rt') as fp:
	for line in fp:
		if line[0] == '#': continue
		words = line.split()
		if words[2] != 'CDS': continue
		beg = int(words[3])
		end = int(words[4])
		lengths.append(end - beg + 1)
print(lengths)
		
"""
lengthstrial = []
path = '../MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz'
with gzip.open(path, 'rt') as filepath:
	for line in filepath:
		if line[0] != '#': 
			words = line.split()
			if words[2] == 'CDS': 
				beg = int(words[3])
				end = int(words[4])
				lengthstrial.append(end - beg + 1)
print(lengthstrial)
		