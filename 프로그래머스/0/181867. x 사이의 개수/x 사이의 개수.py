def solution(myString):
    answer = []
    array = myString.split("x")
    
    for a in array:
        answer.append(len(a))
    return answer