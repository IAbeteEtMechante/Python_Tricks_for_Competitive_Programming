"""
This is an example file of fastIO, from jimm89
I didnt test it, but I put it here for future reference
it is solving this problem:
https://codeforces.com/contest/1487/problem/E
"""


"""
#If FastIO not needed, use this and don't forget to strip
#import sys, math
#input = sys.stdin.readline
"""

import os
import sys
from io import BytesIO, IOBase

BUFSIZE = 8192

class FastIO(IOBase):
    newlines = 0
 
    def __init__(self, file):
        import os
        self.os = os
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
 
    def read(self):
        while True:
            b = self.os.read(self._fd, max(self.os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
 
    def readline(self):
        while self.newlines == 0:
            b = self.os.read(self._fd, max(self.os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
 
    def flush(self):
        if self.writable:
            self.os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)
 
 
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")
 
 
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

from collections import defaultdict as dd

"""
We can compress the options?
Match each A with its best remaining B
"""

N1, N2, N3, N4 = [int(s) for s in input().split()]
A, B, C, D = [int(s) for s in input().split()], [int(s) for s in input().split()], [int(s) for s in input().split()], [int(s) for s in input().split()]
A = [(a,i) for i,a in enumerate(A)]
B = [(a,i) for i,a in enumerate(B)]
C = [(a,i) for i,a in enumerate(C)]
D = [(a,i) for i,a in enumerate(D)]
A.sort()
m1 = dd(set)
m2 = dd(set)
m3 = dd(set)
M1 = int(input())
for m in range(M1):
    x, y = [int(s) for s in input().split()]
    x -= 1
    y -= 1
    m1[y].add(x)
M2 = int(input())
for m in range(M2):
    x, y = [int(s) for s in input().split()]
    x -= 1
    y -= 1
    m2[y].add(x)
M3 = int(input())
for m in range(M3):
    x, y = [int(s) for s in input().split()]
    x -= 1
    y -= 1
    m3[y].add(x)
NEW_A = []
for j in range(N2):
    idx = 0
    while idx < len(A) and A[idx][1] in m1[B[j][1]]:
        idx += 1
    if idx < N1:
        NEW_A.append((A[idx][0]+B[j][0],B[j][1]))
if not NEW_A:
    print(-1)
    sys.exit(0)
NEW_A.sort()
NEW_B = []
for j in range(N3):
    idx = 0
    while idx < len(NEW_A) and NEW_A[idx][1] in m2[C[j][1]]:
        idx += 1
    if idx < len(NEW_A):
        NEW_B.append((NEW_A[idx][0]+C[j][0],C[j][1]))
if not NEW_B:
    print(-1)
    sys.exit(0)
NEW_B.sort()
ans = 10**18
for j in range(N4):
    idx = 0
    while idx < len(NEW_B) and NEW_B[idx][1] in m3[D[j][1]]:
        idx += 1
    if idx < len(NEW_B):
        ans = min(ans,NEW_B[idx][0]+D[j][0])
        
print(ans if ans < 10**18 else -1)
