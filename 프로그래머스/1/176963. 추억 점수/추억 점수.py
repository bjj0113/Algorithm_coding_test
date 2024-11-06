def solution(name, yearning, photo):
    answer = []
    yname = dict(zip(name,yearning))
   #print(yname)
    for x in photo:
        sumy = 0
        for y in x:
            if y in yname:
                sumy += yname[y]
        answer.append(sumy)
    return answer