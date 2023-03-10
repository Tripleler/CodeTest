# https://www.acmicpc.net/problem/16139

from itertools import accumulate
from sys import stdin

input = stdin.readline
s = input().rstrip()
q = int(input())
arr = [[0] * (len(s) + 1) for _ in range(26)]
for i, x in enumerate(s, start=1):
    arr[ord(x) - 97][i] = 1
arr = [list(accumulate(x)) for x in arr]
for _ in range(q):
    x, a, b = input().split()
    a = int(a)
    b = int(b) + 1
    print(arr[ord(x) - 97][b] - arr[ord(x) - 97][a])
