def solution(numbers):
    answer = []
    for i in numbers:
        numbers2=numbers.copy()
        numbers2.remove(i)
        for j in numbers2:
            answer.append(i+j)

    return sorted(list(set(answer)))
print(solution([2,1,3,4,1]), solution([5,0,2,7]))