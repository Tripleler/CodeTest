def solution(k, dungeons):
    from itertools import permutations
    answer = []
    for i in permutations(dungeons):
        st = k
        cnt = 0
        for j in i:
            if j[0] <= st:
                st -= j[1]
                cnt += 1
            else:
                pass
            if st <= 0:
                answer.append(cnt)
                break
        answer.append(cnt)
    return max(answer)


print(solution(80, [[80, 20], [50, 40], [30, 10]]))
