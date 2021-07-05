def isStackFull():
    global SIZE, stack, top
    if (top >= SIZE-1):
        return True
    else:
        return False

def push(data):
    global SIZE, stack, top
    if (isStackFull()):
        print('스택 꽉!')
        return
    if (isStackEmpty()):
        print('아직 공간이 남아있습니다')
    top += 1
    stack[top] = data

def isStackEmpty():
    global SIZE, stack, top
    if (top <= SIZE-1):
        return True
    else:
        return False

def pop():
    global SIZE, stack, top
    # 비었는지 체크


    # 데이터를 추출해서 리턴
    return pop

SIZE = 5
stack = ['커피','녹차','꿀물','콜라',None]
top = 3

print(stack)
push('환타')
print(stack)
push('사이다')
print(stack)