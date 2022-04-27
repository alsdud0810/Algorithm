import sys
n=int(input())
arr=[]

for _ in range(n):
    s,e=map(int, sys.stdin.readline().rstrip().split())
    arr.append([s,e])

arr.sort(key=lambda x: (x[1],x[0]))

cnt=1

end=arr[0][1]
for i in range(1,n):
    if arr[i][0]>=end:
        cnt+=1
        end=arr[i][1]

print(cnt)