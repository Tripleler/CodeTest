def solution(n):
    cnt = bin(n).count('1')
    for i in range(1, n):
        if bin(n + i).count('1') == cnt:
            break
    return int(bin(n + i), 2)


print(solution(78), solution(15))
