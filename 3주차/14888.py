import sys

N=int(sys.stdin.readline().rstrip())
data = list(map(int,sys.stdin.readline().split()))

a,b,c,d = map(int, input().split())
maxx,minn=-sys.maxsize-1, sys.maxsize

def solution(sum, idx, add, sub, mul, div):
    global maxx, minn
    # 계산 끝에 왔을 때, 최댓값과 최솟값이 될 수 있는 지
    if idx == N:
        maxx = max(maxx,sum)
        minn = min(minn,sum)
        return
    # 백트래킹으로 재귀 (각 연산자 개수가 0이 될 때까지)
    if add>0:
        solution(sum+data[idx],idx+1,add-1,sub,mul,div)
    if sub>0:
        solution(sum-data[idx],idx+1,add,sub-1,mul,div)
    if mul>0:
        solution(sum*data[idx],idx+1,add,sub,mul-1,div)
    if div>0:
        solution(int(sum/data[idx]),idx+1,add,sub,mul,div-1)


solution(data[0],1,a,b,c,d)
print(maxx)
print(minn)