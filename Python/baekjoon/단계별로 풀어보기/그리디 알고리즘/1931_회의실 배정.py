# https://www.acmicpc.net/problem/1931

n = int(input())
r = [tuple(list(map(int, input().split()))) for _ in range(n)]
r.sort(key=lambda x: (x[1], x[0]))
answer = 1
end = r[0][1]
for i in range(1, n):
    if r[i][0] >= end:
        answer += 1
        end = r[i][1]
print(answer)
