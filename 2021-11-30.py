import sys

n = int(sys.stdin.readline())
stack = []

for i in range(n):
    order = sys.stdin.readline().split()

    if order[0] == 'push':
        stack.append(order[1])
    
    elif order[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop(0))
    
    elif order[0] == 'size':
        print(len(stack))

    elif order[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif order[0] == 'front':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[0])

    elif order[0] == 'back':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])