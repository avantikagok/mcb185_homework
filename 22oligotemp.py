def tm(A, C, G, T):
	oligolen = A + C + G + T
	if oligolen <= 13:
		melttemp = (A + T) * 2 + (G + C) * 4
		return oligolen, melttemp
	else:
		melttemp = 64.9 + 41 * (G + C - 16.4) / (A + C + G + T)
		return oligolen, melttemp
		
oligolen, melttemp = tm(10, 2, 4, 5)
print("Sequence length:", str(oligolen), "Melting temp:", str(melttemp))

oligolen, melttemp = tm(1, 2, 1, 5)
print("Sequence length:", str(oligolen), "Melting temp:", str(melttemp))

oligolen, melttemp = tm(123984, 223423, 132423, 523423)
print("Sequence length:", str(oligolen), "Melting temp:", str(melttemp))