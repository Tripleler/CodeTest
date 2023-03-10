# https://www.acmicpc.net/problem/11047

from sys import stdin

input = stdin.readline
n, k = map(int, input().split())
m = [int(input()) for _ in range(n)]
answer = 0
for c in reversed(m):
    cnt, k = divmod(k, c)
    answer += cnt
print(answer)
