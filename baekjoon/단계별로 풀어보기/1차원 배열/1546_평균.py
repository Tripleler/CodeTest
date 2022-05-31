# https://www.acmicpc.net/problem/1546

_ = input()
li = list(map(int, input().split()))
print(sum(li) / len(li) / max(li) * 100)
