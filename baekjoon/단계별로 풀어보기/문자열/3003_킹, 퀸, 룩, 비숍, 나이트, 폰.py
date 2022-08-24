# https://www.acmicpc.net/problem/3003

a = [1, 1, 2, 2, 2, 8]
b = map(int, input().split())
for x, y in zip(a, b):
    print(x - y, end=" ")
