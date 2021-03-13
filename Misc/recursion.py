import sys
import threading


def solve():
	#your code goes here
	#you can call other fucntion using global variables too
	#remmeber to use Python, not PyPy!!
	print("OK")




sys.setrecursionlimit(3*10**5)
threading.stack_size(8*10**7)
t = threading.Thread(target=solve)
t.start()
t.join()
