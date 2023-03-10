# https://www.acmicpc.net/problem/25305

n, k = map(int, input().split())
scores = sorted(map(int, input().split()))
print(scores[n - k])
