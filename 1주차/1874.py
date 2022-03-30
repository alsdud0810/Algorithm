# 구글 코드 참고
import sys

N=int(sys.stdin.readline())
stack=[]
result=[]
flag=0
num=1

for _ in range(N):
    x=int(sys.stdin.readline())
    while num<=x:
        stack.append(num)
        result.append("+")
        num+=1
    
    if stack[-1]==x:
        stack.pop()
        result.append("-")

    else:
        print("NO")
        flag=1
        break

if flag==0:
    for i in result:
        print(i)