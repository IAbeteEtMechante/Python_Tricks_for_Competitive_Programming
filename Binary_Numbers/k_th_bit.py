# Python 3 program to find
# k-th bit from right
 
def getKthBit(n, k):

 
    return (n & (1 << (k - 1))) >> (k - 1)
 
# Driver Code
n = 13
k = 2
 
# Function Call
print(getKthBit(n, k))  # Binary representation of 13 is 1101. Second bit from right is 0.