def scoringmatrix(nts):
	# Print first line
	print('   ', end='')
	for nt1 in nts:
		print(nt1, end=('  '))
	print()
	
	#Print individual lines
	for nt2 in nts:	
		print(nt2, end=' ')
		for nt1 in nts:
			if nt1 == nt2: 
				print('+1', end=' ')
			else:
				print('-1', end=' ')
		print('')

scoringmatrix('ACGT')
scoringmatrix('ACGTNSLKDFJSKDJ')

