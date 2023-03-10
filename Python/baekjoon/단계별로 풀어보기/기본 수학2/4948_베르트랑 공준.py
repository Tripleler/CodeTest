# https://www.acmicpc.net/problem/4948

prime = [False, False] + [True] * 123456 * 2
for i, cond in enumerate(prime):
    if cond:
        prime[2 * i::i] = [False] * len(prime[2 * i::i])
while True:
    n = int(input())
    if not n:
        break
    cnt = 1 if n < 2 else 0
    for i in range(n + (2 if n % 2 else 1), 2 * n + 1, 2):
        if prime[i]:
            cnt += 1
    print(cnt)
