def solution(x, n):
    answer = [0] * n
    num = x
    for i in range(n) :
        answer[i] = num
        num += x
        
    return answer