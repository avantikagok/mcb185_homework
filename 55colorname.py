import sys

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])


input = (R, G, B)
def dtc(P, Q):
    d = 0
    for p, q in zip(P, Q):
        d += abs(p - q)
    return d 
    
colordatabase = []
distance = []
with open(colorfile) as fp:
    for line in fp:
    	colordatabase.append(line)
    	colorline = line.split()
    	vals = colorline[2]
    	vals = vals.split(',')
    	intvals = (int(vals[0]), int(vals[1]), int(vals[2]))
    	distance.append(dtc(input, intvals))

min = distance[0]
for i in distance[1:]:
	if i < min: 
		min = i
	
for index, i in enumerate(distance):
	if i == min:
		colordetails = colordatabase[index].split()
		print(colordetails[0])


	



