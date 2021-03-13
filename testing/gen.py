import random
import sys
import numpy as np
import string

#create bounds for numbers
LOW = 1
HIGH = 10

ALPHABET = np.array(list(string.ascii_lowercase))

def generate_integer(low, high):
	"""
	generate random integer between low and high (both included)
	"""
	return random.randint(low, high)


def generate_list_integers(low, high, size):
	"""
	generate a string 
	of random numbers between low and high (both included)
	size of the string: size
	"""
	return " ".join([str(x) for x in np.random.randint(low=low, high=high + 1, size=size)])


def generate_string(n):
    return "".join(np.random.choice(ALPHABET, size=n))


# print('Number of arguments:', len(sys.argv), 'arguments.')
# print ('Argument List:', str(sys.argv))

#read command line arguments
N = int(sys.argv[1])
n= generate_integer(low = 2, high = N )
m = generate_integer(low = 1, high = 2*n )
s = generate_integer(low = 1, high = n)



print(n,m,s)

for i in range(m):
	a,b,w= generate_integer(1, n), generate_integer(1, n), generate_integer(-HIGH, HIGH)
	print(a,b,w)
