import sys

t=int(sys.stdin.readline().rstrip())

for _ in range(t):
    n=int(sys.stdin.readline().rstrip())
    data = list(map(int,sys.stdin.readline().split()))
    data.sort(reverse=True)

    dif=0
    max=0
    for i in range(n-2):
        dif= data[i]-data[i+2]
        if dif>max:
            max=dif
    print(max)