import sys
import heapq

n=int(input())

arr=[]
for _ in range(n):
    p,d=map(int, sys.stdin.readline().rstrip().split())
    arr.append([p,d])

arr.sort(key=lambda x: x[1])

result=[]

for i in arr:
    heapq.heappush(result,i[0])
    if len(result) >i[1]:
        heapq.heappop(result)

print(sum(result))