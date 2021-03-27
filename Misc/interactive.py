from collections import *
import sys  

# "". join(strings)  
    
def ri():
    return int(input())
 
def rl():
    return list(map(int, input().split()))

low = 1
high = 1000000

while (low < high):
	guess = high - (high - low)//2
	print(guess, flush= True)
	sign = input()
	if sign =='<':
		high = guess - 1
	else:
		low = guess
print("!", low)
