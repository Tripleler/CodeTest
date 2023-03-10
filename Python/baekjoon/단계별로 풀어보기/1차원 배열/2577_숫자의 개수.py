from sys import stdin
from collections import Counter

result = 1
for _ in range(3):
    result *= int(*stdin.readline().split())

result = str(result)

for i in range(10):
    print(Counter(result)[str(i)])
