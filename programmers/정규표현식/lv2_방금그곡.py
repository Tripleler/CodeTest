def solution(m, musicinfos):
    answer = []
    import re
    p1 = re.compile('[a-zA-Z]#?')
    p2 = re.compile('[A-Z]#')
    m = p2.sub(lambda x: x[0].lower(), m)
    cnt = 0
    for i in musicinfos:
        i = p2.sub(lambda x: x[0].lower(), i)
        music = i.split(',')
        time = 60 * (int(music[1].split(':')[0]) - int(music[0].split(':')[0])) + (
                int(music[1].split(':')[1]) - int(music[0].split(':')[1]))
        info = p1.findall(music[3])
        melody = []
        for _ in range(time // len(info)):
            melody += info
        for j in range(time % len(info)):
            melody.append(info[j])
        if m in ''.join(melody):
            answer.append((time, music[2]))
            cnt += 1
    if len(answer) == 0:
        answer = "(None)"
    else:
        answer.sort(key=lambda x: -x[0])
        answer = answer[0][1]
    return answer


print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
