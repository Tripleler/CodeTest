# https://www.acmicpc.net/problem/9012

from sys import stdin

input = stdin.readline
for _ in range(int(input())):
    s = input().rstrip()
    while '()' in s:
        s = s.replace('()', '')
    print('NO' if s else 'YES')
