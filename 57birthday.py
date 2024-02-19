import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

totalsuccess = 0


calendar = []
monthlist = []
for month in range(1, 13):
	if month in (9, 4, 6, 11):
		lastdayofmonth = 30
	elif month == 2:
		if days == 365: 
			lastdayofmonth = 28
		else:
			lastdayofmonth = 29
	else:
		lastdayofmonth = 31

	for day in range(1, lastdayofmonth + 1):
		monthlist.append([day, 0])
	calendar.append(monthlist)
	monthlist = []

#print(calendar)
		
for trial in range(1, trials + 1):
	trialsuccess = 0
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
		
		calendar[month - 1][day - 1][1] += 1
		if calendar[month - 1][day - 1][1] >= 2:
			trialsuccess += 1 
		
#resetting counts in calendar	 
	for i in calendar:
		for j in i:
			j[1] = 0
			
	if trialsuccess != 0:
		totalsuccess += 1
		
					

print('Successful trials:', totalsuccess)
print('Total trials:', trials)
print(totalsuccess / trials)
			
						
		




