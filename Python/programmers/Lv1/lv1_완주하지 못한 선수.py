def solution(participant, completion):
    participant.sort()
    completion.sort()
    if participant[-1] != completion[-1]:
        answer = participant[-1]
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
    return answer

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))