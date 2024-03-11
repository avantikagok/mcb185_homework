d = {}
d = dict()

d = {'dog': 'woof', 'cat': 'meow'}
print(d)

print(d['cat'])

d['pig'] = 'oink'
print(d)

d['cat'] = 'mew'
print(d)

del d['cat']
print(d)

if 'dog' in d: print(d['dog'])

for key in d: print(f'{key} says {d[key]}')

for k, v in d.items(): print(k, 'says', v)

for thing in d.items(): print(thing[0], thing[1])

print(d.keys(), d.values(), list(d.values()))

'''
count = {}
for nt in seq:
    if nt not in count: count[nt] = 0
    count[nt] += 1
'''
    
import itertools
for nts in itertools.product('ACGT', repeat=2):
    print(nts)
    
    
    
    
seq = 'ABCDEFGHIJK'
for i in range(0, len(seq), -1): 
	print(seq)
	print(seq[i])
	



import mcb185

seq = 'ATGC'
antiseq = mcb185.anti_seq(seq)

print(seq)
print(antiseq)

i = 1
print(seq[i])
print(antiseq[len(seq) - i - 1])
	
