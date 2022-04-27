import sys
import heapq

n=int(input())

arr=[]

for _ in range(n):
    s,e=map(int, sys.stdin.readline().rstrip().split())
    arr.append([s,e])
arr.sort()

room=[]
heapq.heappush(room,arr[0][1]) #첫번째 강의 종료 시간

for i in range(1,n):
    if arr[i][0]<room[0]:
        heapq.heappush(room,arr[i][1])
    else: #아니면, 바로 이어서 강의 -> 방 만들 필요 없음.
        heapq.heappop(room)
        heapq.heappush(room,arr[i][1])
print(len(room))
