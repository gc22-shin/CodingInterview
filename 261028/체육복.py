##https://school.programmers.co.kr/learn/courses/30/lessons/42862#

def solution(n, lost, reserve):
    answer = 0
    
    lost_ = [l for l in lost]

    for l in lost:
        if l in reserve:
            lost_.remove(l)
            reserve.remove(l)

    lost_.sort()
    lost.sort()
    reserve.sort()
    #print(lost)
    
    
    for l in lost:
        print(lost, reserve)
        if l in lost_ and l - 1 in reserve:
            lost_.remove(l)
            reserve.remove(l-1)
        elif l in lost_ and l + 1 in reserve:
            lost_.remove(l)
            reserve.remove(l + 1)
            
    answer = n - len(lost_)
    
    return answer




### set 활용 풀이 ###
def solution(n, lost, reserve):
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)

    answer = n - len(lost_set)

    for l in sorted(lost_set):
        if l - 1 in reserve_set:
            reserve_set.remove(l - 1)
            answer += 1
        elif l + 1 in reserve_set:
            reserve_set.remove(l + 1)
            answer += 1

    return answer
