import sys
import heapq

N=int(input())
heap=[]

for _ in range(N):
    x=int(sys.stdin.readline())
    if x!=0:
        heapq.heappush(heap,-x)
    else:
        if len(heap)==0:
            print(0)
        else:
            print(heapq.heappop(heap)*(-1))