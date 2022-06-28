# https://www.acmicpc.net/problem/5086

from sys import stdin

input = stdin.readline
while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    if b // a == b / a:
        print('factor')
    elif a // b == a / b:
        print('multiple')
    else:
        print('neither')
