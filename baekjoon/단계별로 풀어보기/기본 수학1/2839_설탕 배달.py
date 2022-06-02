# https://www.acmicpc.net/problem/2839

n = int(input())
if n in [4, 7]:
    print(-1)
else:
    i = 0
    while n % 5:
        n -= 3
        i += 1
    print(i + n // 5)
