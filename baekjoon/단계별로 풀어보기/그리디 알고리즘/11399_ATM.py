# https://www.acmicpc.net/problem/11399

n = int(input())
l = sorted(list(map(int, input().split())), reverse=True)
answer = 0
for i, j in zip(range(1, n + 1), l):
    answer += i * j
print(answer)
