import collections
import string
import math
import copy
import os
import sys
from io import BytesIO, IOBase

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
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


def input(): return sys.stdin.readline().rstrip("\r\n")


# n = 0
# m = 0

# n = int(input())

# li = [int(i) for i in input().split()]

# s = sorted(li)
"""
from dataclasses import dataclass

@dataclass
class point:
    x: float
    y: float
 
 
@dataclass
class line:
    A: float
    B: float
    C: float
 
    def gety(self, x):
        return (self.A*x+self.C)/-self.B
    
    def getx(self, y):
        return (self.B*y+self.C)/-self.A
 
    def k(self):
        return -self.A/self.B
 
    def b(self):
        return -self.C/self.B
 
    def dist(self, p: point):
        return abs((self.A*p.x+self.B*p.y+self.C)/(self.A**2+self.B**2)**0.5)
 
 
def calc_line(u: point, v: point):
    return line(A=u.y-v.y, B=v.x-u.x, C=u.y*(u.x-v.x)-u.x*(u.y-v.y))
 
 
def is_parallel(u: line, v: line) -> bool:
    f1 = False
    f2 = False
    try:
        k1 = u.k()
    except:
        f1 = True
    try:
        k2 = v.k()
    except:
        f2 = True
    if f1 != f2:
        return False
    return f1 or k1 == k2
 
 
def seg_len(_from: point, _to: point):
    return ((_from.x - _to.x)**2 + (_from.y - _to.y)**2) ** 0.5
 
def in_range(_from: point, _to: point, _point: point) -> bool:
    if _from.x < _to.x:
        if _from.y < _to.y:
            return _from.x <= _point.x <= _to.x and _from.y <= _point.y <= _to.y
        else:
            return _from.x <= _point.x <= _to.x and _from.y >= _point.y >= _to.y
    else:
        if _from.y < _to.y:
            return _from.x >= _point.x >= _to.x and _from.y <= _point.y <= _to.y
        else:
            return _from.x >= _point.x >= _to.x and _from.y >= _point.y >= _to.y
 
def intersect(u: line, v: line) -> point:
    tx = (u.B*v.C-v.B*u.C)/(v.B*u.A-u.B*v.A)
    if u.B!=0.0:
        ty = -u.A*tx/u.B - u.C/u.B
    else:
        ty = -v.A*tx/v.B - v.C/v.B
    return point(x=tx, y=ty)
 
def in_direction(_from: point, _to: point, _point: point) -> bool:
    if _from.x < _to.x:
        if _from.y < _to.y:
            return _to.x < _point.x  and _to.y < _point.y
        else:
            return _to.x < _point.x  and _point.y <= _to.y
    else:
        if _from.y < _to.y:
            return _to.x >= _point.x  and _to.y < _point.y
        else:
            return _to.x >= _point.x  and _point.y <= _to.y


"""
mo = int(1e9+7)


def exgcd(a, b):
    if not b:
        return 1, 0
    y, x = exgcd(b, a % b)
    y -= a//b * x
    return x, y


def getinv(a, m):
    x, y = exgcd(a, m)
    return -1 if x == 1 else x % m


def comb(n, b):
    res = 1
    b = min(b, n-b)
    for i in range(b):
        res = res*(n-i)*getinv(i+1, mo) % mo
        # res %= mo
    return res % mo


def quickpower(a, n):
    res = 1
    while n:
        if n & 1:
            res = res * a % mo
        n >>= 1
        a = a*a % mo
    return res


def dis(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


def getpref(x):
    if x > 1:
        return (x)*(x-1) >> 1
    else:
        return 0


def orafli(upp):
    primes = []
    marked = [False for i in range(upp+3)]
    prvs = [i for i in range(upp+3)]
    for i in range(2, upp):
        if not marked[i]:
            primes.append(i)
        for j in primes:
            if i*j >= upp:
                break
            marked[i*j] = True
            prvs[i*j] = j
            if i % j == 0:
                break
    return primes, prvs


def lower_ord(c: str) -> int:
    return ord(c)-97


def upper_ord(c: str) -> int:
    return ord(c) - 65


def read_list():
    return [int(i) for i in input().split()]


def read_int():
    s = input().split()
    if len(s) == 1:
        return int(s[0])
    else:
        return map(int, s)


def ask(s):
    print(f"? {s}", flush=True)


def answer(s):
    print(f"{s}", flush=True)


def solve():
    # n,m = read_int()
    n = read_int()
    s = input()
    a = ['' for i in s]
    b = []
    # b = ['' for i in s]
    c1 = s.count('1')
    if s[0]!='1' or s[-1]!='1' or c1&1:
        print('NO')
        return
    ctc = 0
    sta = 0
    for p, i in enumerate(s):
        if i=='1':
            ctc+=1
            if ctc<=c1//2:
                a[p] = '('
            else:
                a[p] = ')'
        else:
            if sta:
                a[p] = ')'
            else:
                a[p] = '('
            sta^=1
    for p, i in enumerate(s):
        if i=='0':
            if a[p]=='(':
                b.append(')')
            else:
                b.append('(')
        else:
            b.append(a[p])
    print('YES')
    print(''.join(a))
    print(''.join(b))
    # for p, i in enumerate(b):


    
"""
1
14
10001110001111
"""

    
# fi = open('C:\\cppHeaders\\CF2020.12.17\\test.data', 'r')
# def input(): return fi.readline().rstrip("\r\n")
# primes, prv = orafli(10001)
# solve()
t = int(input())

for ti in range(t):
    # print(f"Case #{ti+1}: ", end='')
    solve()