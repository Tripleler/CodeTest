# https://programmers.co.kr/learn/courses/30/lessons/12973?language=python3

def solution(s):
    stack = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif stack[-1] != i:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop(-1)
    answer = 1 if len(stack) == 0 else 0
    return answer


print(solution('baabaa'))
print(solution('cdcd'))
