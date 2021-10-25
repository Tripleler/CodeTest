def solution(s):
    n = 0
    for i in s:
        if i == '(':
            n += 1
        else:
            n -= 1
        if n < 0:
            break
    if n != 0:
        return False
    else:
        return True


print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))
