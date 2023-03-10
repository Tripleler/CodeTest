# https://www.acmicpc.net/problem/11729


def hanoi(i):
    global s
    if i < n:
        li = []
        for x in s:
            li.append(switch(x, True))
        li += [[1, 3]]
        for x in s:
            li.append(switch(x, False))
        s = li.copy()
        hanoi(i + 1)


def switch(old_li, cond):
    li = old_li.copy()
    if cond:
        if li[0] == 2:
            li[0] = 3
        elif li[0] == 3:
            li[0] = 2
        if li[1] == 2:
            li[1] = 3
        elif li[1] == 3:
            li[1] = 2
    else:
        if li[0] == 1:
            li[0] = 2
        elif li[0] == 2:
            li[0] = 1
        if li[1] == 1:
            li[1] = 2
        elif li[1] == 2:
            li[1] = 1
    return li


n = int(input())
print(2 ** n - 1)
s = [[1, 3]]
hanoi(1)
for j in s:
    print(j[0], j[1])
