import sys

stack=[]

def push(x):
    stack.append(x)

def pop():
    if len(stack)==0:
        return -1
    else:
        return stack.pop()

def size():
    return len(stack)

def empty():
    if len(stack)==0:
        return 1
    else:
        return 0
def top():
    if len(stack)==0:
        return -1
    else:
        return stack[-1]

N=int(input())
heap=[]

for _ in range(N):
    x=sys.stdin.readline().split()
    scan=x[0]

    if scan=="push":
        push(x[1])
    elif scan=="pop":
        print(pop())
    elif scan=="size":
        print(size())
    elif scan=="empty":
        print(empty())
    elif scan=="top":
        print(top())