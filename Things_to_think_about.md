# Things to think about
Random ideas from previous problems


## Graphs
* If you have a graph with n vertices and n edges, you are basically having a tree + one edge. Then you always have exactly one cycle in that graph

## Strings
* Palindromes: every palindrome contains a palindrome of length 2 or 3 (may be himself)

## work with numbers and digits
* sometimes it is better to convert a number to a string for easier manipulation:
n = 15645234
digits = str(n) 
len(digits) # 8
digits[-2] = 3 
(it is faster than having to think about dividing by all the powers of 10 and take reminder and make a list)

