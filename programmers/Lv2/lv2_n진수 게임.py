def solution(n, t, m, p):
    dic = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    s1 = '0'
    for num in range(n * t * m):
        s2 = ''
        while num > 0:
            num, mod = divmod(num, n)
            if mod >= 10:
                s2 += dic[mod]
            else:
                s2 += str(mod)
        s1 += s2[::-1]
        if len(s1) > m * t:
            break
    answer = s1[p - 1::m][:t]
    return answer


print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))
