# https://www.acmicpc.net/problem/2559

n, k = map(int, input().split())
l = list(map(int, input().split()))
c = sum(l[:k])
l2 = [c]
for i in range(n - k):
    c += l[i + k] - l[i]
    l2.append(c)
print(max(l2))
