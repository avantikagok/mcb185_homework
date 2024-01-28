def hydrophobicityval(letter):
	if letter == 'R':
		value = -4.5
		return value 
	elif letter == 'K':
		value = -3.9
		return value
	elif letter == 'D':
		value = -3.5
		return value
	elif letter == 'Q':
		value = -3.5
		return value
	elif letter == 'N':
		value = -3.5
		return value
	elif letter == 'E':
		value = -3.5
		return value
	elif letter == 'H':
		value = -3.2
		return value
	elif letter == 'P':
		value = -1.6
		return value
	elif letter == 'Y':
		value = -1.3
		return value
	elif letter == 'W':
		value = -0.9
		return value
	elif letter == 'S':
		value = -0.8
		return value
	elif letter == 'T':
		value = -0.7
		return value
	elif letter == 'G':
		value = -0.4
		return value
	elif letter == 'A':
		value = 1.8
		return value
	elif letter == 'M':
		value = 1.9
		return value
	elif letter == 'C':
		value = 2.5
		return value
	elif letter == 'F':
		value = 2.8
		return value
	elif letter == 'L':
		value = 3.8
		return value
	elif letter == 'V':
		value = 4.2
		return value
	elif letter == 'I':
		value = 4.5
		return value
	else:
		value = "This letter does not signify an amino acid"
		return value
		
		
value = hydrophobicityval('K')
print(value)

value = hydrophobicityval('B')
print(value)

value = hydrophobicityval('V')
print(value)