# https://www.acmicpc.net/problem/3036

import math

input()
l = list(map(int, input().split()))
k = l[0]
for i in l[1:]:
    x = math.gcd(k, i)
    print(f'{k // x}/{i // x}')
