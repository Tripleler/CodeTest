# https://www.acmicpc.net/problem/2884

hour, minute = map(int, input().split())
t = hour * 60 + minute - 45
if t < 0:
    t += 1440
print(t // 60, t % 60)
