# https://www.acmicpc.net/problem/1871

from sys import stdin

n = int(input())
for i in range(n):
    s, num = stdin.readline().split('-')
    a = sum([(ord(x) - 65) * 26 ** (2 - j) for j, x in enumerate(s)])
    b = int(num)
    if abs(a - b) <= 100:
        print('nice')
    else:
        print('not nice')
