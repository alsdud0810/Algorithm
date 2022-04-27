n=int(input())
arr=list(map(int,input().split()))

arr.sort(reverse=False)

plus=0
sum=0

for i in range(n):
    plus+=arr[i]
    sum+=plus

print(sum)