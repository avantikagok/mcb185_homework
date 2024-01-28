import math 
import sys 

def entropy(a, c, g, t):
	tot = a + c + g + t


	a_prob = a / tot
	c_prob = c / tot
	g_prob = g / tot
	t_prob = t / tot
	
	h = 0
	if a != 0:
		h = h + a_prob * math.log2(a_prob)
	if c != 0:
		h = h + c_prob * math.log2(c_prob)
	if g != 0:
		h = h + g_prob * math.log2(g_prob)
	if t != 0:
		h = h + t_prob * math.log2(t_prob)
		
	h_final = -1 * h
	
	return h_final
		

ans = entropy(1, 3, 5, 19)
print("H equals:", ans)
	 
	 
ans = entropy(23, 3, 5, 19)
print("H equals:", ans)

ans = entropy(0, 6, 2, 4)
print("H equals:", ans)

ans = entropy(100, 123, 5123, 191)
print("H equals:", ans)