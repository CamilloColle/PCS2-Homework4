from itertools import *

with open("rosalind_lexf.txt") as f:
    s = ''.join(f.readline().split())
    n = int(f.readline())


for i in product(s, repeat = n):
    print(''.join(i))

