# https://www.acmicpc.net/problem/2525

hour, minute = map(int, input().split())
t = hour * 60 + minute + int(input())
if t >= 1440:
    t -= 1440
print(t // 60, t % 60)
