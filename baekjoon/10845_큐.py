# https://www.acmicpc.net/problem/10845

from sys import stdin

n = int(input())
queue = []
for _ in range(n):
    s = stdin.readline()
    try:
        if s.startswith('push'):
            queue.append(int(s.split()[-1]))
        elif s.startswith('pop'):
            print(queue.pop(0))
        elif s.startswith('size'):
            print(len(queue))
        elif s.startswith('empty'):
            print(0) if queue else print(1)
        elif s.startswith('front'):
            print(queue[0])
        elif s.startswith('back'):
            print(queue[-1])
    except:
        print(-1)
