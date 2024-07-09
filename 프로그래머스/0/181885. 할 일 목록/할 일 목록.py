def solution(todo_list, finished):
    answer = []
    for i,x in enumerate(todo_list):
        if finished[i] == False:
            answer.append(x)
            
    return answer