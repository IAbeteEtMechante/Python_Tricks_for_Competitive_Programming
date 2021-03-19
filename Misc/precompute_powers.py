"""
It is really simple code, but if you use the powers of a given number many times 
you should think to precompute those powers
"""


def precompute_powers(n = 2, max_pow = 10):
	powers = [1]
	for i in range(max_pow + 1):
	    powers.append(powers[-1] * n)
	return powers


#driving code:
pow2 = precompute_powers(2,10)
print(pow2)