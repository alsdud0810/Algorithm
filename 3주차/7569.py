import sys
from collections import deque

m,n,h = map(int, sys.stdin.readline().split())

graph = []

#이동할 방향 정의
dx=[-1,1,0,0,0,0]
dy=[0,0,1,-1,0,0]
dz=[0,0,0,0,1,-1]

#큐 구현을 위해 deque 라이브러리 사용
queue = deque()

for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int,sys.stdin.readline().split())))
        for k in range(m):
            if tmp[j][k]==1:
                queue.append([i,j,k])
    graph.append(tmp)

#bfs 소스코드 구현
def bfs():
    while queue:
        x,y,z=queue.popleft()
        for i in range(6):
            nx=x+dx[i]
            ny=y+dy[i]
            nz=z+dz[i]

            if 0<=nx<h and 0 <= ny < n and 0<=nz<m and graph[nx][ny][nz] == 0:
                graph[nx][ny][nz]=graph[x][y][z]+1
                queue.append((nx,ny,nz))
                
bfs()
result=0
for i in graph:
    for j in i:
        for k in j:
            if k==0:
                print(-1)
                exit(0)
        result = max(result, max(j))
print(result-1)