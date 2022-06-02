# https://www.acmicpc.net/problem/10250

for _ in range(int(input())):
    h, _, n = map(int, input().split())
    a, b = divmod(n, h)
    if b:
        a += 1
    else:
        b = h
    print(f'{b}{"0" + str(a) if a < 10 else a}')

# for _ in range(int(input())):
#     h, _, n = map(int, input().split())
#     a, b = divmod(n - 1, h)
#     print(100 * (b + 1) + (a + 1))
