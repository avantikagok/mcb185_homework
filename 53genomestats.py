import gzip
import sys


gffpath = sys.argv[1]
feature = sys.argv[2]
lengthstrial = []

with gzip.open(gffpath, 'rt') as fp:
	for line in fp:
		if line[0] != '#': 
			words = line.split()
			if words[2] == feature: 
				beg = int(words[3])
				end = int(words[4])
				lengthstrial.append(end - beg + 1)
print('Count:', len(lengthstrial))



def minmax(somelist):
	minimum = somelist[0]
	maximum = somelist[0]
	for val in somelist:
		if val < minimum: minimum = val
		if val > maximum: maximum = val
	return minimum, maximum

def meanstd(somelist):
	meantotal = 0
	for val in somelist:
		meantotal += val
		meanval = int(meantotal / len(somelist))
	stdtotal = 0
	for val in somelist:
		stdtotal += (val - meanval) ** 2
	stdev = int((stdtotal / len(somelist)) ** 0.5)
	return meanval, stdev

def median(somelist):
	somelist.sort()
	median1 = int((len(somelist) / 2) - 0.5)
	median2 = int((len(somelist) / 2) + 0.5)
	if len(somelist) % 2 == 0:
		median = (somelist[median1] + somelist[median2]) / 2
	else:
		median = somelist[median1]
	return int(median)

min, max = minmax(lengthstrial)
print('Minimum:', min, 'Maximum:', max)
mean, std = meanstd(lengthstrial)
print('Mean:', mean)
print('Standard Deviation', std)
medval = median(lengthstrial)
print('Median:', medval)

