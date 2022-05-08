import sys
from collections import deque

m,n = map(int, sys.stdin.readline().split())

graph = [list(map(int, input().split())) for _ in range(n)]

#이동할 네 가지 방향 정의(상,하,좌,우)
dx=[-1,1,0,0]
dy=[0,0,-1,1]

#큐 구현을 위해 deque 라이브러리 사용
queue = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])

#bfs 소스코드 구현
def bfs():
    #큐가 빌 때까지 반복하기
    while queue:
        x,y=queue.popleft()
        #현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))
                
bfs()
result=0
for i in graph:
    for j in i:
        if j==0:
            print(-1)
            exit(0)
    result = max(result, max(i))
print(result-1)