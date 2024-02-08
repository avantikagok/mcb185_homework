import random

def normalsavingthrow(dc):
	dicethrow = random.randint(1, 20)
	if dicethrow >= dc:
		outcome = 'success'
	else:
		outcome = 'failure'
	return outcome

def normalprob(dc):
	successcount = 0
	failurecount = 0
	for i in range(1, 10001):
		outcome = normalsavingthrow(dc)
		if outcome == 'success':
			successcount += 1
		else:
			failurecount += 1
	successprob = successcount / 10000
	failureprob = failurecount / 10000
	return successprob
	

def advsavingthrow(dc):
	dicethrow1 = random.randint(1, 20)
	dicethrow2 = random.randint(1, 20)
	maxdicethrow = 0
	if dicethrow1 > dicethrow2:
		maxdicethrow = dicethrow1
	else:
		maxdicethrow = dicethrow2
	if maxdicethrow >= dc:
		outcome = 'success'
	else:
		outcome = 'failure'
	return outcome 
	
def dissavingthrow(dc):
	dicethrow1 = random.randint(1, 20)
	dicethrow2 = random.randint(1, 20)
	mindicethrow = 0
	if dicethrow1 > dicethrow2:
		mindicethrow = dicethrow2
	else:
		mindicethrow = dicethrow1
	if mindicethrow >= dc:
		outcome = 'success'
	else:
		outcome = 'failure'
	return outcome 

def advprob(dc):
	successcount = 0
	failurecount = 0
	for i in range(1, 10001):
		outcome = advsavingthrow(dc)
		if outcome == 'success':
			successcount += 1
		else:
			failurecount += 1
	successprob = successcount / 10000
	failureprob = failurecount / 10000
	return successprob 

def disprob(dc):
	successcount = 0
	failurecount = 0
	for i in range(1, 10001):
		outcome = dissavingthrow(dc)
		if outcome == 'success':
			successcount += 1
		else:
			failurecount += 1
	successprob = successcount / 10000
	failureprob = failurecount / 10000
	return successprob
	
print('', 'Normal', 'Adv', 'Disadv', sep='\t')	
print('DC 5', normalprob(5), advprob(5), disprob(5), sep='\t')
print('DC 10', normalprob(10), advprob(10), disprob(10), sep='\t')
print('DC 15', normalprob(15), advprob(15), disprob(15), sep='\t')
