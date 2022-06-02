# https://www.acmicpc.net/problem/2675

for _ in range(int(input())):
    answer = ''
    n, s = input().split()
    for x in s:
        answer += x * int(n)
    print(answer)
