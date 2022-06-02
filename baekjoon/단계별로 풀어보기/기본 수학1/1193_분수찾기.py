# https://www.acmicpc.net/problem/1193

import math

x = int(input())
n = math.ceil(((1 + 8 * x) ** 0.5 - 1) / 2)
i = x - int(n * (n - 1) / 2)
print(f'{n - i + 1}/{i}' if n % 2 else f'{i}/{n - i + 1}')
