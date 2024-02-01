nts = 'ACGT'

print('   ', end='')
for nt1 in nts:
	if nt1 != 'T': 
		print(nt1, end=('  '))
	else:
		print(nt1)


for nt2 in nts:	
	print(nt2, end=' ')
	for nt1 in nts:
		if nt1 == nt2: 
			print('+1', end=' ')
		else:
			print('-1', end=' ')
	print('')

	
