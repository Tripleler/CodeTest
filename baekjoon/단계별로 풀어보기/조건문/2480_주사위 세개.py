# https://www.acmicpc.net/problem/2480

scores = sorted(map(int, input().split()))
if len(set(scores)) == 1:
    print(10000 + int(scores[0]) * 1000)
elif len(set(scores)) == 2:
    print(1000 + scores[1] * 100)
else:
    print(int(scores[-1]) * 100)
