# 노드 삽입 함수의 완성

class Node():
    def __init__(self):
        self.node = None
        self.link = None

def printNodes(start):
        current = start
        if current == None:
            return
        print(current.data, end=' ')
        while current.link != None:
            current = current.link
            print(current.data, end=' ')
        print()

def insertNode(findData, insertData):
        global memory, head, current, pre

        if head.data == findData: # 첫번째 노드 삽입
            node = Node()
            node.data = insertData
            node.link = head
            head = node
            return

        current = head
        while current.link != None: # 중간 노드 삽입
            pre = current
            current = current.link
            if current.data == findData:
                node = Node()
                node.data = insertData
                node.link = current
                pre.link = node
                return

        node = Node()   # 마지막 노드 삽입
        node.data = insertData
        current.link = node


# 전역 변수 선언
memory = []

head, current, pre = None,None,None

# import random
# dataArray = [random.randint(1000,9999) for _ in range(20)]

dataArray = ['다현','장연','쯔위','사나','지효']


# 메인 코드 부분
if __name__ == '__main__':

    node = Node()
    node.data = dataArray[0]  # 첫번째 노드
    head = node
    memory.append(node)

    for data in dataArray[1:]:  # 두번째 노드 이후
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)

    printNodes(head)

    insertNode('다현','화사')
    printNodes(head)

    insertNode('사나','솔라')
    printNodes(head)

    insertNode('재남','문별')
    printNodes(head)



