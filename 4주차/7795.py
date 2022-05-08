import sys
import bisect

N=int(sys.stdin.readline().rstrip())

for _ in range(N):
    s,m=map(int, sys.stdin.readline().rstrip().split())
    dataa = list(map(int,sys.stdin.readline().split()))
    dataa.sort()
        
    datab = list(map(int,sys.stdin.readline().split()))
    datab.sort()
    sum=0
    for i in datab:
        sum+=(s-(bisect.bisect(dataa,i)))
        #bisiect.bisect는 insert위치+1 반환.
        #오름차순 정렬에서 insert했으므로 s에서 빼준 것이
        #a가 큰 경우의 개수이다.
    print(sum)