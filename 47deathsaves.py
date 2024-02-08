import random

def deathsaves():
	failure = 0
	success = 0
	thrownum = 1
	status = True
	while status: 
		throw = random.randint(1, 20)
		if throw >= 10:
			if throw == 20:
				status = False
				statusdef = 'revived'
			else:
				success += 1
		else:	
			if throw == 1:
				failure += 2
			else:
				failure += 1	
		if failure >= 3:
			status = False
			statusdef = 'death'
		if success >= 3:
			status = False
			statusdef = 'stable'	
	return(statusdef)
	

deathcount = 0
stablecount = 0
revivecount = 0	

for i in range(1, 10001):
	trial = deathsaves()
	if trial == 'death':
		deathcount += 1
	if trial == 'stable':
		stablecount += 1
	if trial == 'revived':
		revivecount += 1
		
print(f'Death prob {deathcount / 10000}, Stable prob {stablecount / 10000}, Revive prob {revivecount / 10000}')
	

		