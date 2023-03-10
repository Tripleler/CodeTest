# https://www.acmicpc.net/problem/2231

n = input()
m = len(n) * 9
n = int(n)
cond = True
for i in range(max(n - m, 1), n):
    c = sum(map(int, list(str(i))))
    if i + c == n:
        print(i)
        cond = False
        break
if cond:
    print(0)
