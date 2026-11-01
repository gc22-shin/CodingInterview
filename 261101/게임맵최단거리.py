#https://school.programmers.co.kr/learn/courses/30/lessons/1844

def solution(maps):
    answer = -1
    N = len(maps)
    M = len(maps[0])
    #0 = 벽, 1 = 길
    
    def movable(i, j, N, M):
        if 0 <= i and i < N:
            if 0 <= j and j < M:
                return maps[i][j] == 1
        return False
            
    
    
    def BFS(N, M):
        from collections import deque
        dis, djs = [1, -1, 0, 0], [0, 0, 1, -1]
        visited = [[False for _ in range(M)] for _ in range(N)]
        
        q = deque()
        q.append([0,0, 1])
        visited[0][0] = True
        
        while q:
            i, j, curr_dist = q.popleft()
            #print(i, j, curr_dist, q)

            for di, dj in zip(dis, djs):
                new_i = i + di
                new_j = j + dj
                if movable(new_i, new_j, N, M):
                    if not visited[new_i][new_j]:
                        if new_i == N - 1 and new_j == M - 1:
                            return curr_dist + 1
                        q.append([new_i, new_j, curr_dist + 1])
                        visited[new_i][new_j] = True
        return -1
                                                  
    answer = BFS(N, M)
    
    return answer



#이렇게도 가능
while q:
    for _ in range(len(q)):
        i, j = q.popleft()

        if (i, j) == (N-1, M-1):
            return dist

        for di, dj in directions:
            ni, nj = i + di, j + dj

            if movable(ni, nj) and not visited[ni][nj]:
                visited[ni][nj] = True
                q.append((ni, nj))

    dist += 1
