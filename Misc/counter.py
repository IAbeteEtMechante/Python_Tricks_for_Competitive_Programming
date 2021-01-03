#this file is very hard to read, better run it in order to understand how to use Counter
from collections import Counter
import sys

input = sys.stdin.readline

def rl():
	return list(map(int, input().split()))

# aa = rl()

aa = [2,5,1,4,7,1,1,12]

C = Counter(aa)


print("\nSimple display of the Counter:")
print(C)

#can use C as a dict, whose keys are the values of aa:
print("\nCounter is a Python dict, whose keys are the values of aa, each appearing just one time (no repetitions):")
print("C.keys():")


####### All keys ###########
for val in C.keys():
	print(val, end = " ")
print()
###########################

#can see the 1 most common element of aa:
print("\nGet the most common element of aa, as a pair (most common val, freq):")
print("C.most_common(1)[0]")

########Most Common value of aa###############
common_val, freq = C.most_common(1)[0]
#############################################


print("most common val:", common_val, "freq:",freq)
print("**be careful, needed to add the [0] in the previous expression, because most_common(1) is a list containing just one element, that element being a tuple (val, freq)")
print("you could change most_common(1) to most_common(3) if you want the 3 most common values, not super usefull i guess though.**")


#can see the list of all pairs (element of aa, frequency) in descending order:
print("\nAll values of aa in decreasing order of frequency: (val, freq) pairs, with freq decreasing")

print("C.most_common()")
###########################
print(C.most_common())
###########################


print("\nSo to get the least common element, we take the last element of the previous list of pairs:")\


#############Least Common value of aa##################
least_common_val, smallest_freq = C.most_common()[-1]
######################################################


print("C.most_common()[-1]")
print("val: ", least_common_val, "freq:",smallest_freq)
