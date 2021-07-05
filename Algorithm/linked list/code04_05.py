# 단순 연결 리스트의 일반 형태

# 클래스와 함수 선언 부분
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    if current == None:
        return
    print(current.data, end = ' ')
    while current.link != None:
        current = current.link
        print(current.data, end = ' ')
    print()


# 전역 변수 선언 부분
memory = []

head, current, pre = None,None,None

# import random
# dataArray = [random.randint(1000,9999) for _ in range(20)]
dataArray = ['다현','정연','쯔위','사나','지효']

# 메인 코드 부분
if __name__ == '__main__':

    node = Node()
    node.data = dataArray[0] # 첫번째 노드
    head = node
    memory.append(node)

    for data in dataArray[1:]: # 두번째 노드 이후
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)

    printNodes(head)

