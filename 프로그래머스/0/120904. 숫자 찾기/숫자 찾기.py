def solution(num, k):
    nu = list(str(num))
    
    for i in range(len(nu)):
        if(int(nu[i]) == k):
            return i+1
    return -1
