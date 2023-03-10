# https://www.acmicpc.net/problem/10870

n = int(input())
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    a = 0
    b = 1
    answer = 0
    for _ in range(n - 1):
        a, b = b, a + b
    print(b)
