from collections import Counter


def solution(id_list, report, k):
    report = list(set(report))
    answer = [0 for _ in id_list]
    a = []  # 신고된 리스트
    b = []  # k번 이상인 리스트
    for name in report:
        a.append(name.split()[1])
    for key, val in Counter(a).items():
        if val >= k:
            b.append(key)
    for name in report:
        if name.split()[1] in b:
            answer[id_list.index(name.split()[0])] += 1
    return answer


print(
    solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
             2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
