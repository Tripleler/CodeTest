# https://www.acmicpc.net/problem/2004

def div(x, y, z, n):
    cnt = 0
    while x >= n:
        x //= n
        cnt += x
    while y >= n:
        y //= n
        cnt -= y
    while z >= n:
        z //= n
        cnt -= z
    return cnt


a, b = map(int, input().split())
b = min(a - b, b)
c = a - b
print(max(min(div(a, b, c, 2), div(a, b, c, 5)), 0))
