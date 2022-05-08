import sys

N=int(input())

data = list(map(int,sys.stdin.readline().split()))


data.sort()

print(data[(N-1)//2])

