# 연결 리스트(Linked List)
# 컴퓨터과학에서 배열과 함께 가장 기본이 되는 대표적인 선형 자료구조 중 하나
# 다양한 추상 자료형(Abstract Data Type) 구현의 기반이 된다

# Q13. 팰린드롬 연결 리스트
# 연결 리스트가 팰린드롬 구조인지 판별하라

# 풀이 01 // 리스트 변환
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