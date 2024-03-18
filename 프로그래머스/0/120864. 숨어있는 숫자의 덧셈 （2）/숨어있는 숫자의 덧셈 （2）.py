def solution(my_string):
    answer = 0
    inx = 0
    for x in my_string:
        if(x.isalpha()):
            my_string = my_string.replace(x," ")
            
    a = my_string.split()
    
    for y in a:
        answer += int(y)
    return answer