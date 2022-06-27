# https://www.acmicpc.net/problem/4153

while True:
    l = sorted(list(map(int, input().split())))
    if not sum(l):
        break
    print('right' if l[0] ** 2 + l[1] ** 2 == l[2] ** 2 else 'wrong')
