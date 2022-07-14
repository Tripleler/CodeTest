# https://www.acmicpc.net/problem/10828

from sys import stdin

n = int(input())
stack = []
for _ in range(n):
    s = stdin.readline()
    try:
        if s.startswith('push'):
            stack.append(int(s.split()[-1]))
        elif s.startswith('pop'):
            print(stack.pop(-1))
        elif s.startswith('size'):
            print(len(stack))
        elif s.startswith('empty'):
            print(0) if stack else print(1)
        elif s.startswith('top'):
            print(stack[-1])
    except:
        print(-1)
