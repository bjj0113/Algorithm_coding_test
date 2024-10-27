def solution(picture, k):
    answer = []
    for x in picture:
        pic = ''
        for y in x:
            for _ in range(k):
                pic += y
        for _ in range(k):
            answer.append(pic)
    return answer