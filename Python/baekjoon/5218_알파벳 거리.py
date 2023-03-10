from sys import stdin

n = int(input())
for _ in range(n):
    a, b = stdin.readline().split()
    num = len(a)
    s = ''
    for x, y in zip(a, b):
        s += ' '
        s += str(ord(y) - ord(x) + 26) if ord(y) - ord(x) < 0 else str(ord(y) - ord(x))
    print(f'Distances:{s}')
