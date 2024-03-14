import sys
import mcb185
import gzip
import json

def read_transfac(filepath):
	output = []
	with gzip.open(filepath, 'rt') as fp:
		for line in fp:
			if line.startswith('ID'): 
				line = line.split()
				idname = line[1]
			elif line.startswith('PO'):
				record = {'ID': idname, 'pwm': []}
				for line in fp:
					if line.startswith('XX'):
						output.append(record)
						break
					else:
						#print(line)
						words = line.split()
						positiondict = {
							"A": float(words[1]),
							"C": float(words[2]),
							"G": float(words[3]),
							"T": float(words[4])
							}
						record['pwm'].append(positiondict)
			
						

	print(json.dumps(output, indent=4))
				

filepath = sys.argv[1]
read_transfac(filepath)
