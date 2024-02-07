import random

def normal3d6():
	normal = (random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)) 
	return(normal)
 
def diff3d6r1():
	r1 = 0
	rollnumber = 1
	while rollnumber <= 3:  
		roll = random.randint(1, 6)
		if roll != 1:
			r1 += roll
			rollnumber +=1
	return(r1)

def diff3d6x2():
	x2 = 0
	for i in range(4):
		roll1 = random.randint(1, 6)
		roll2 = random.randint(1, 6)
		if roll1 > roll2:
			x2 += roll1
		else:
			x2 += roll2
	return(x2)
		
def diff4d6d1():
	roll1 = random.randint(1, 6)
	roll2 = random.randint(1, 6)
	roll3 = random.randint(1, 6)
	roll4 = random.randint(1, 6)
	if roll1 < roll2:
		lowest = roll1
	else:
		lowest = roll2
	if roll3 < lowest:
		lowest = roll3
	if roll4 < lowest:
		lowest = roll4
	d1 = roll1 + roll2 + roll3 + roll4 - lowest
	return(d1)		
	
	


def averagescores(limit):
	totalnormal = 0
	totalr1 = 0
	totalx2 = 0
	totald1 = 0
	for i in range(limit):
		normalnewval = normal3d6()
		totalnormal += normalnewval
		r1newval = diff3d6r1()
		totalr1 += r1newval
		x2newval = diff3d6x2()
		totalx2 += x2newval
		d1newval = diff4d6d1()
		totald1 += d1newval
	print(f'3D6 average: {totalnormal / limit}, 3D6r1 average: {totalr1 / limit}, 3d6x2 average: {totalx2 / limit}, 4D6d1 average: {totald1 / limit}')
	


averagescores(10000)
# how do you do this without making them functions