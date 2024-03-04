import sys
import mcb185
import math 


def entropy(a, c, g, t, frame):

	a_prob = a / frame
	c_prob = c / frame
	g_prob = g / frame
	t_prob = t / frame
	
	h = 0
	if a != 0:
		h = h + a_prob * math.log2(a_prob)
	if c != 0:
		h = h + c_prob * math.log2(c_prob)
	if g != 0:
		h = h + g_prob * math.log2(g_prob)
	if t != 0:
		h = h + t_prob * math.log2(t_prob)
		
	h_final = -1 * h
	
	return h_final


w = int(sys.argv[2])
threshold = float(sys.argv[3])
seqlist = []
outputlist = []


for defline, seq in mcb185.read_fasta(sys.argv[1]):
	for i in seq:
		seqlist.append(i)
		outputlist.append(i)
	for i in range(0, len(seq) - w + 1):
		window = seqlist[i:i+w]
		a = window.count('A')
		c = window.count('C')
		g = window.count('G')
		t = window.count('T')
		if entropy(a, c, g, t, w) <= threshold:
			for j in range(i, i + w + 1):
				outputlist[j] = 'N'

finalstring = ''
for i in range(0, len(outputlist)): 
	finalstring += outputlist[i]
	
for i in range(0, len(finalstring), 60):
	print(finalstring[i:i+60])
