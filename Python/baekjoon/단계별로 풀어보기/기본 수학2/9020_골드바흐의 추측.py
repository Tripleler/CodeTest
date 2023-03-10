# https://www.acmicpc.net/problem/9020

prime = [False, False] + [True] * 10000
for i, cond in enumerate(prime):
    if cond:
        prime[2 * i::i] = [False] * len(prime[2 * i::i])
for _ in range(int(input())):
    n = int(input())
    if n == 4:
        print(2, 2)
        continue
    a = b = n // 2
    if not a % 2:
        a -= 1
        b += 1
    while True:
        if prime[a] and prime[b]:
            print(a, b)
            break
        else:
            a -= 2
            b += 2
