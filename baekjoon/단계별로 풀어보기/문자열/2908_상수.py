# https://www.acmicpc.net/problem/2908

a, b = map(lambda x: int(x[::-1]), input().split())
print(a if a > b else b)
