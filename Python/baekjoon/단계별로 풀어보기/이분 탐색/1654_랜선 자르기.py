# https://www.acmicpc.net/problem/1654

k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]
left = 1
right = max(lines)
while left <= right:
    mid = (right + left) // 2
    cnt = 0
    for line in lines:
        cnt += (line // mid)
    if cnt >= n:
        left = mid + 1
    else:
        right = mid - 1
print(right)
