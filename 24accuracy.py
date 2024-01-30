def accuracy(TP, FP, TN, FN):
	return (TP + TN) / (TP + TN + FP + FN) 

def f1(TP, FP, TN, FN):
	return (2 * TP) / (2 * TP + FP + FN)

def performance(TP, FP, TN, FN):
	return accuracy(TP, FP, TN, FN), f1(TP, FP, TN, FN)
	

print(performance(1, 2, 3, 4))
	
print(performance(5, 2, 3, 5))