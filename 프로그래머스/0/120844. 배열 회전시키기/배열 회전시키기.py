def solution(numbers, direction):
    answer = []
    if(direction == "right"):
        numbers.insert(0,numbers[-1])
        numbers.pop(-1)
    else:
        numbers.append(numbers[0])
        numbers.pop(0)
    return numbers