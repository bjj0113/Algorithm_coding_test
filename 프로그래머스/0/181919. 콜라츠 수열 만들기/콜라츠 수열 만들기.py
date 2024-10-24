answer = []

def solution(n):
    answer.append(n)
    if n % 2 == 0:
        n = n/2
        return solution(n)
    elif n == 1:
        return answer
    else:
        n = 3 * n +1
        return solution(n)
    
    return answer
    