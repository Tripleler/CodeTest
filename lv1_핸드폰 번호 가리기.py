def solution(phone_number):
    answer=''
    answer+='*'*(len(phone_number)-4)
    answer+=phone_number[-4:len(phone_number)]
    return answer
print(solution("01033334444"))
