import sys

#n이 가로, m이 세로
n,m=map(int, sys.stdin.readline().rstrip().split())
a=[list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
b=[list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

cnt=0

for i in range(n-2):
    for j in range(m-2):
        if a[i][j]!=b[i][j]: #값이 다르면
            for x in range(3):
                for y in range(3):
                    a[i+x][j+y]=1-a[i+x][j+y]
            cnt+=1
if a==b:
    print(cnt)
else:
    print("-1")