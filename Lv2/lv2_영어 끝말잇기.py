def solution(n, words):
    answer = [0, 0]
    li = []
    cnt = None
    for i in range(len(words) - 1):
        li.append(words.pop(0))
        if not (words[0].startswith(li[-1][-1]) & (words[0] not in li)):
            cnt = i + 2
            break
    if cnt != None:
        answer = []
        answer.append(cnt % n if cnt % n != 0 else n)
        answer.append(((cnt - 1) // n) + 1)
    return answer


print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5,
               ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang",
                "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
