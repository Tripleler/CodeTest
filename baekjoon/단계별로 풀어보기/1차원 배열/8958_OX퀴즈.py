# https://www.acmicpc.net/problem/8958

n = int(input())
for _ in range(n):
    score = 0
    cum = 1
    for c in input():
        if c == 'O':
            score += cum
            cum += 1
        else:
            cum = 1
    print(score)
