def solution(table, languages, preference):
    table.sort()
    score_list=[]
    score=0
    for i in table:
        subject=i.split(' ')
        for j in range(len(languages)):
            try:
                score+=(6-subject.index(languages[j]))*preference[j]
            except:
                pass
        score_list.append(score)
        score=0
    answer=table[score_list.index(max(score_list))].split(' ')[0]
    return answer
table = [["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
          "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
          "GAME C++ C# JAVASCRIPT C JAVA"],
         ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
          "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
          "GAME C++ C# JAVASCRIPT C JAVA"]]
languages = [["PYTHON", "C++", "SQL"], ["JAVA", "JAVASCRIPT"]]
preference = [[7, 5, 5], [7, 5]]
for i, j, k in zip(table, languages, preference):
    print(solution(i, j, k))