import sys
import math

probs = []
for arg in sys.argv[1:]:
	prob = float(arg)
	assert(prob > 0 and prob <= 1)
	probs.append(prob)
	
total = 0
for p in probs: 
	total += p
if not math.isclose(total, 1.0):
	sys.exit('Error: probabilities do not sum to 1')
	
hval = 0
for p in probs:
	hval += p * math.log2(p)
	

print(-1 * hval)