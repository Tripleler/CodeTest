# https://www.acmicpc.net/problem/10992

n = int(input())
for i in range(n):
    print(' ' * (n - 1 - i) + '*' + ('*' if i == n - 1 else ' ') * (2 * i - 1) + ('*' if i else ''))