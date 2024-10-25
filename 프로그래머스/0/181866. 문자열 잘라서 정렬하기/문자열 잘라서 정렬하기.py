def solution(myString):
    answer = []
    answer = myString.split('x')
    answer.sort()
    for _ in range(len(answer)):
        if "" in answer:
            answer.remove("")
    return answer