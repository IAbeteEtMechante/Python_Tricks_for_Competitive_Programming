#remove() throws error if the element not in the set

#but discard() has no error 

ss = set([1,2,3])

#no error
ss.discard(4)

ss.discard(3)
print(ss)

