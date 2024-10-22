def solution(my_string, is_prefix):
    answer = 0
    if is_prefix in my_string and my_string[len(is_prefix)-1] == is_prefix[len(is_prefix)-1] and my_string[0] == is_prefix[0]:
        answer = 1
    return answer