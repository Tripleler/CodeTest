# https://www.acmicpc.net/problem/1010

from sys import stdin
import math

input = stdin.readline
for _ in range(int(input())):
    a, b = sorted(map(int, input().split()))
    print(math.comb(b, a))
