# 문자열 조작
# - 문자열을 변경하거나 분리하는 등 여러 과정
# - 로우 레벨에서 조작하거나 C처럼 문자형이 따로 없는 언어에서는 조작이 까다롭다
# - 단, 대부분의 언어는 별도의 문자열 자료형과 문자열 조작을 위한 다양한 기능을 제공한다

# 문자열 처리와 관련된 알고리즘이 쓰이는 분야
# - 정보처리 분야 : 여러 키워드로 웹 페이지를 탐색할 때 문자열 처리 애플리케이션을 이용
# - 통신 시스템 분야 : 문자 메시지나 이메일을 보낼 때, 문자열을 어느 한 곳에서 다른곳으로 보냄
# - 프로그래밍 시스템 분야 : 프로그램 자체가 문자열로 구성, 컴파일러나 인터프리터 등은 문자열을 해석하고 처리하여 기계어로 변환하는 역할을
#   하는데 여기에 매우 정교한 문자열 처리 알고리즘이 쓰인다

# 실습 01 유호한 팰린드롬 (팰린드롬 : 앞뒤가 똑같은 문장 :) 다시합창합시다)
# Q 주어진 문자열이 팰린드롬인지 확인하라.  대소문자를 구분하지 않으며 영문자와 숫자만을 대상으로 한다.

# - 입력
# 예제 1 : 'A man, a plan, a canal: Panama'
# 예제 2 : 'race a car'

# 풀이 1. 리스트 변환 == 문자열을 직접 입력받아 팰린드롬 여부 판별하기

class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum(): # isalnum(): 영문자, 숫자 여부 판별하여 False, True 변환
                strs.append(char.lower()) # 모든 문자 소문자 변환하여 str에 입력
                print('문자처리: ', strs)
        
        # 팰린드롬 여부 판별
        while len(strs) > 1: # strs의 길이가 1 이상이면 반복

            #pop(0) : 맨 앞의 값, pop(): 맨 뒤의 값을 가져옴
            if strs.pop(0) != strs.pop():
                return False
        return True
    
if __name__ == '__main__':
    print('실행합니다: main')
# 현재 스크립트 파일이 프로그램 시작점이 맞는지 판단
# 스크립트 파일이 메인 프로그램으로 사용될 때와 모듈로 사용될 때를 구분하기 위해서
    s = Solution()
    print(s.isPalindrome('A man, a plan, a canal : Panama'))
    print(s.isPalindrome('race a car'))

# 풀이 2. 데크 자료형을 이용한 최적화
# 데크(deque)를 명시적으로 선언하여 풀이 속도 개선하기
# - deque: double-ended queue 양방향에서 데이터를 처리할 수 있는 queue 형 자료구조

import collections
from typing import Deque

class Solution:
    def is_Palindrome(self, s: str) -> bool:

        # 자료형 데크로 선언
        strs : Deque = collections.deque() # 데크 생성
        print('\n데크 생성 :', strs)

        for char in s:
            if char.isalnum():
                strs.append(char.lower())
                print('문자 처리: ', strs)
        while len(strs) > 1:
            if strs.popleft() != strs.pop(): # 데크의 popleft()는 0(1), 리스트의 pop(0)이 0(n)
                return False
        
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.is_Palindrome('A man, a plan, a canal : Panama'))
    print(s.is_Palindrome('race a car'))
