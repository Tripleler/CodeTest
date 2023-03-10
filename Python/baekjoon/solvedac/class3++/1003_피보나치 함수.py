# https://www.acmicpc.net/problem/1003

for _ in range(int((input()))):
    n = int(input())
    if n == 0:
        print('1 0')
    elif n == 1:
        print('0 1')
    else:
        f = [0, 1]
        for i in range(2, n + 1):
            f.append(f[i - 2] + f[i - 1])
        print(f[-2], f[-1])
