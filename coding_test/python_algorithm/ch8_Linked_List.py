# 연결 리스트(Linked List)
# 컴퓨터과학에서 배열과 함께 가장 기본이 되는 대표적인 선형 자료구조 중 하나
# 다양한 추상 자료형(Abstract Data Type) 구현의 기반이 된다

# Q13. 팰린드롬 연결 리스트
# 연결 리스트가 팰린드롬 구조인지 판별하라

# 풀이 01 // 리스트 변환
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def pylist(self, head: ListNode) -> bool:
        q: List = []

        if not head:
            return True

        node = head
        # 리스트 변환
        while node is not None:
            q.append(node.val)
            node = node.next

        # 팰린드롬 판별
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False

        return True

if __name__ == '__main__':
  s = Solution()
  li = ListNode(1) # li = [1]
  li.next = ListNode(2) # li = [1,2]
  print(s.pylist(li))
  li.next.next = ListNode(2) # li = [1,2,2]
  li.next.next.next = ListNode(1) # li = [1,2,2,1]
  print(s.pylist(li))

# 풀이 02 // 데크 이용
  # 데크를 이용한 최적화
import collections
class Solution:
    def pydeque(self, head: ListNode) -> bool:
        # 데크 자료형 선언
        q: Deque = collections.deque()

        if not head:
            return True

        node = head
        # 리스트 변환
        while node is not None:
            q.append(node.val)
            node = node.next

        # 팰린드롬 판별
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False

        return True

if __name__ == '__main__':
  s = Solution()
  li = ListNode(1) # li = [1]
  li.next = ListNode(2) # li = [1,2]
  print(s.pydeque(li))
  li.next.next = ListNode(2) # li = [1,2,2]
  li.next.next.next = ListNode(1) # li = [1,2,2,1]
  print(s.pydeque(li))

  class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # 예외 처리
        if head is None:
            return None

        odd = head
        even = head.next
        even_head = head.next

        # 반복하면서 홀짝 노드 처리
        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        # 홀수 노드의 마지막을 짝수 헤드로 연결
        odd.next = even_head
        return head

s = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next= ListNode(5)
answer = s.oddEvenList(l1)
while answer is not None:
  print(f'{answer.val}', end=" ")
  answer = answer.next
