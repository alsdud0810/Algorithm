import sys

t=int(input())


for _ in range(t):
    arr=[]
    N=int(sys.stdin.readline())
    for _ in range(N):
        s,m=map(int, sys.stdin.readline().rstrip().split())
        arr.append([s,m])
    arr.sort()
    n2=arr[0][1] #첫번째 사람 면접 등수
    count=1
    for i in range(N):
        comp=arr[i][1] #비교: 면접등수
        if comp<n2: #비교하는 사람이 등수가 좋으면
            n2=comp #n2에 비교하는 사람
            count+=1 #등수가 안뒤지니까 카운트

    print(count)
