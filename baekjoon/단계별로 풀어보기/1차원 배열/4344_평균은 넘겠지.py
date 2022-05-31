# https://www.acmicpc.net/problem/4344

n = int(input())
for _ in range(n):
    scores = list(map(int, input().split()))[1:]
    mean = sum(scores) / len(scores)
    i = 0
    for score in scores:
        if score > mean:
            i += 1
    print('{:.3f}%'.format(round(i / len(scores) * 100, 3)))
