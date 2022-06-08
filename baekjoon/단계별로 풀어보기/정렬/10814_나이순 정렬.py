# https://www.acmicpc.net/problem/10814

from sys import stdin

input = stdin.readline
li = []
for _ in range(int(input())):
    age, name = input().split()
    li.append(tuple((int(age), name)))
for i, j in sorted(li, key=lambda x: x[0]):
    print(i, j)
