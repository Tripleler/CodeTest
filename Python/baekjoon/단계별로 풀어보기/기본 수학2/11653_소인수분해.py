# https://www.acmicpc.net/problem/11653

n = int(input())
cond = True
for i in range(2, int(n ** 0.5) + 1):
    while not n % i:
        print(i)
        n //= i
        cond = False
if n > 1:
    print(n)
