# https://programmers.co.kr/learn/courses/30/lessons/92342?language=python3

def solution(n, info):
    win_shot = [((10 - i) * 2, x + 1, i) if x else ((10 - i), x + 1, i) for i, x in enumerate(info)]
    win_shot = sorted(win_shot, key=lambda x: (-x[0] / x[1], -x[1]))
    print(win_shot)
    shot_li = []
    ix_li = []
    lion = 0
    for score, shot, ix in win_shot:
        if n >= shot:
            shot_li.append(shot)
            ix_li.append(ix)
            n -= shot
            lion += int(score / shot)
            if not n:
                break
    peach = sum([(10 - i) if x and i not in ix_li else 0 for i, x in enumerate(info)])
    print(peach, lion)
    if peach >= lion:
        return [-1]
    else:
        answer = [0 for _ in range(11)]
        for i in range(len(ix_li)):
            answer[ix_li[i]] = shot_li[i]
        mod_shot = sum(info) - sum(answer)
        if mod_shot:
            answer[10] = mod_shot
        return answer


# print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
# print(solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
# print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))
# print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))
print(solution(9, [3, 0, 0, 0, 0, 0, 0, 0, 0, 1, 5]))
