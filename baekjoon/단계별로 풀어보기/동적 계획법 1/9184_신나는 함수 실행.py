# https://www.acmicpc.net/problem/9184

from sys import stdin

input = stdin.readline

dic = {}


def w(a, b, c):
    global dic
    try:
        return dic[tuple([a, b, c])]
    except KeyError:
        if a <= 0 or b <= 0 or c <= 0:
            return 1
        elif a > 20 or b > 20 or c > 20:
            return 1048576
        elif a < b < c:
            dic[tuple([a, b, c])] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
            return dic[tuple([a, b, c])]
        else:
            dic[tuple([a, b, c])] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
            return dic[tuple([a, b, c])]


while True:
    a, b, c = map(int, input().split())
    if (a == -1) * (b == -1) * (c == -1):
        break
    print(f'w({a}, {b}, {c}) = {w(a, b, c)}')
