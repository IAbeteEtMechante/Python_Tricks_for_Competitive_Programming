# Things to think about
Random ideas from previous problems


## Graphs
* If you have a graph with n vertices and n edges, you are basically having a tree + one edge. Then you always have exactly one cycle in that graph

## Strings
* Palindromes: every palindrome contains a palindrome of length 2 or 3 (may be himself)
* I believe in general it is faster to work with list than strings. Especially if you want to have a string of given length (maybe 200000) that you want to build character by character, it is better to preaffect a list of this lengthm and work with it, than make an empty string and do += (200000 times)  [see this problem](https://codeforces.com/contest/1503/problem/A)

## Work with numbers and digits
* sometimes it is better to convert a number to a string for easier manipulation:
n = 15645234 <br>
digits = str(n) <br>
len(digits) # 8 <br>
digits[-2] = 3 <br>
(it is faster than having to think about dividing by all the powers of 10 and take reminder and make a list, if you have to work with all the digits anyway)

## Function
* sometimes it is nice to numerically approximate the derivative of f
by chosing epsilon very small (= 10^-6 for example) 
and calculate (f(x + epsilon) - f(x - epsilon)) / (2 * epsilon)

