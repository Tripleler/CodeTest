# https://www.acmicpc.net/problem/1934

import math
from sys import stdin

input = stdin.readline
for _ in range(int(input())):
    a, b = sorted(map(int, input().split()))
    print(math.lcm(a, b))
