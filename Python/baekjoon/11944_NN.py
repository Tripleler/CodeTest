N, M = map(int, input().split())
s = str(N) * N
print(s[:min(len(s), M)])
