import dogma
import mcb185
import sys

file = sys.argv[1]
min_length = sys.argv[2]

def find_proteins(trans_seq, min_length):
	valid_proteins = []
	protein = ''
	start_found = False
	
	for aa in trans_seq:
		if aa == 'M' and not start_found:
			start_found = True
			protein += aa
		elif start_found:
			protein += aa
			if aa == '*':
				if len(protein) >= int(min_length):
					valid_proteins.append(protein)
				protein = ''
				start_found = False
	return valid_proteins
	
def six_frame_translation(dna, min_length):
	proteins = []
	frames = [dna, dogma.revcomp(dna)]
	
	for dna_seq in frames:
		for frame in range(3):
			trans_seq = dogma.translate(dna_seq[frame:])
			proteins += find_proteins(trans_seq, min_length)
	return proteins
	
output_proteins = []
for defline, seq in mcb185.read_fasta(file):
	proteins = six_frame_translation(seq, min_length)
	defline = defline.split(' ')[0]
	for i, protein in enumerate(proteins):
		identifier = f'{defline}-prot-{i}'
		output_proteins.append((identifier, protein))

for identifier, protein in output_proteins:
	print(f'>{identifier}')
	for i in range(0, len(protein), 60):
		print(protein[i:i+60])