import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])


totalsuccess = 0

for trial in range(1, trials + 1):
	trialsuccess = 0
	bdlist = []
	for ind in range(1, people + 1):
		month = random.randint(1, 12)
		if month in (9, 4, 6, 11):
			day = random.randint(1, 30)
		elif month == 2:
			if days == 365:
				day = random.randint(1, 28)
			else:
				day = random.randint(1, 29)
		else:	
			day = random.randint(1, 31)
		for i in bdlist:
			if i[0] == month:
				if i[1] == day:
					#print('match')
					trialsuccess += 1
		bdlist.append((month, day))
	if trialsuccess != 0:
		totalsuccess += 1
	#print("----------")

print('Successful trials:', totalsuccess)
print('Total trials:', trials)
print(totalsuccess / trials)
		