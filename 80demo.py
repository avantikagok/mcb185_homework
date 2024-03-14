import mcb185 
import sys
import dogma
import json

seq = 'ABCDE'

print(seq[0:0+3])
print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])

d = [
    'hello',
    (3.14, 'pi'),
    [-1, 0, 1],
    {'year': 2000, 'month': 7}
]
print(d[0][4], d[1][0], d[2][2], d[3]['month'])

seq = 'ABCDEFGHIJKL'

'''
catalog = mcb185.read_catalog(sys.argv[1])
for primer in catalog:
    print(primer['Name'], primer['Description']) 
    
print(dogma.tm('AGCTAC'))

for primer in catalog:
	primer['Tm'] = dogma.tm(primer['Sequence'])
print(catalog)

truc = {
    'animals': {'dog': 'woof', 'cat': 'meow', 'pig': 'oink'},
    'numbers': [1.09, 2.72, 3.14],
    'is_complete': False,
}
print(json.dumps(truc, indent=4))
'''

x = 'seven'
x = int(x)
