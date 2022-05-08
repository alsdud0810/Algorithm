import sys

n,l=map(int, sys.stdin.readline().rstrip().split())

data = list(map(int,sys.stdin.readline().split()))

data.sort()

count=1

s=data[0]   #테이프 비교 시작지점
e=data[0]+l #시작지점부터 테이프 붙일 수 있는 곳

for i in range(n):
    if data[i]+1>e:
        #테이프를 추가하는 시점은
        #위치가 e보다 커지는 시점이다.
        # 즉, 같다면 거기까지 붙이고 멈춘다.
        # 따라서 위치 + 1보다 e가 크다면
        # 테이프 수를 추가하고, s는 커진 위치,
        # e는 s+l임.
        count+=1
        s=data[i]
        e=data[i]+l
print(count)

