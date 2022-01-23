def solution(cacheSize, cities):
    answer = 0
    for i in range(len(cities)):
        cities[i] = cities[i].lower()
    li = []
    for i in cities:
        if i in li:
            answer += 1
            li.remove(i)
            li.append(i)
        else:
            answer += 5
            li.append(i)
            if len(li) == cacheSize + 1:
                li.pop(0)
    return answer


print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(2,
               ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork",
                "Rome"]))
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
