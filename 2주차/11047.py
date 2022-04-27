n,k=map(int, input().split())

arr=[]
cnt=0

for _ in range(n):
    coin=int(input())
    arr.append(coin)

arr.sort(reverse=True)

for i in arr:
    cnt+=k//i
    k%=i
    
print(cnt)