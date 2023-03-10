# https://www.acmicpc.net/problem/1712

import math

a, b, c = map(int, input().split())
print(-1 if c <= b else math.floor(a / (c - b)) + 1)
