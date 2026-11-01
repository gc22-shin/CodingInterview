#https://school.programmers.co.kr/learn/courses/30/lessons/43162

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]

    def BFS(start):
        from collections import deque
        q = deque()
        q.append(start)
        visited[start] = True
        while q:
            curr = q.popleft()
            #print(curr, q, computers[curr])
            for nxt, adj in enumerate(computers[curr]):
                if adj == 1:
                    if not visited[nxt]:
                        q.append(nxt)
                        visited[nxt] = True
    
    for computer in range(n):
        #print(computer)
        if not visited[computer]:
            BFS(computer)
            answer += 1 
        else:
            continue
        #print(visited)

    return answer
