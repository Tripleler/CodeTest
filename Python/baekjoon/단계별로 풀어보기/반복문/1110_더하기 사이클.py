# https://www.acmicpc.net/problem/1110

s = input()
n = int(s)
cycle = 0
while True:
    cycle += 1
    if len(s) == 1:
        s = '0' + s
    s = s[-1] + str(int(s[0]) + int(s[1]))[-1]
    if int(s) == n:
        break
print(cycle)
