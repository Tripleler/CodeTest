# https://www.acmicpc.net/problem/7568

li = []
for _ in range(int(input())):
    li.append(tuple(map(int, input().split())))
rank = []
for i in li:
    cnt = 0
    for j in li:
        if i[0] < j[0] and i[1] < j[1]:
            cnt += 1
    rank.append(str(cnt + 1))
print(' '.join(rank))
