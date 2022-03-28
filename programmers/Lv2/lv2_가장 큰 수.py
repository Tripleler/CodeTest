# https://programmers.co.kr/learn/courses/30/lessons/42746?language=python3

def solution(numbers):
    answer = ''
    length = len(str(max(numbers)))
    numbers = [str(x) for x in numbers]
    numbers.sort(reverse=True, key=len)
    for i, number in enumerate(numbers):
        if len(number) < length:
            if number[0] < number[-1]:
                numbers[i] += '.' + number[0] * (length - len(number)) + ' ' * (length - len(number))
            else:
                numbers[i] += '.' + number[0] * (length - len(number))
    numbers.sort(reverse=True, key=lambda x: x.replace('.', ''))
    for number in numbers:
        answer += number.split('.')[0]
    if answer[0] == '0':
        answer = '0'
    return answer


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
