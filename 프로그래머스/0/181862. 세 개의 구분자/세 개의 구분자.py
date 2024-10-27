def solution(myStr):
    answer = []
    
    x = myStr.replace("a", "c")
    x = x.replace("b", "c")
    x = x.replace("ccc","c")
    x = x.replace("cc","c")
    answer = x.split("c")
    
    while "" in answer:
        answer.remove("")
        
    if not answer:
        answer.append("EMPTY")
        
    return answer