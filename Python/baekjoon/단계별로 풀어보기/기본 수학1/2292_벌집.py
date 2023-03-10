# https://www.acmicpc.net/problem/2292

n = int(input()) - 1
i = 0
while n > 3 * i ** 2 + 3 * i:
    i += 1
print(i + 1)
