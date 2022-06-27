# https://www.acmicpc.net/problem/1358

w, h, x, y, p = map(int, input().split())
cnt = 0
d = [x - h // 2, x, x + w, x + w + h // 2]
r = h // 2
for _ in range(p):
    a, b = map(int, input().split())
    if d[1] <= a <= d[2]:
        if y <= b <= y + h:
            cnt += 1
    elif d[0] <= a < d[1]:
        if (d[1] - a) ** 2 + (y + r - b) ** 2 <= r ** 2:
            cnt += 1
    elif d[2] < a <= d[3]:
        if (d[2] - a) ** 2 + (y + r - b) ** 2 <= r ** 2:
            cnt += 1
print(cnt)
