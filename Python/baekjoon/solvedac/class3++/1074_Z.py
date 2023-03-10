# https://www.acmicpc.net/problem/1074


def z(n, r, c):
    if n == 1:
        return 2 * r + c
    else:
        if r >= 2 ** (n - 1):
            r -= 2 ** (n - 1)
            if c >= 2 ** (n - 1):  # 4사분면
                c -= 2 ** (n - 1)
                k = 3
            else:  # 3사분면
                k = 2
        else:
            if c >= 2 ** (n - 1):  # 2사분면
                c -= 2 ** (n - 1)
                k = 1
            else:  # 1사분면
                k = 0
        return z(n - 1, r, c) + 4 ** (n - 1) * k


n, r, c = map(int, input().split())
print(z(n, r, c))
