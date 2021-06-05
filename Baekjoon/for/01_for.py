# 빠른 A + B

# 입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 날 수 있다
# hint : sys.stdin.readline()
# 단 이때는 맨 끝의 개행문자까지 함께 입력되니 .rstrip() 을 써주는것이 좋다

import sys
T = int(sys.stdin.readline().rstrip())
num = []
for i in range(T):
    A,B = map(int,sys.stdin.readline().rstrip().split())
    C = A + B
    num.append(C)
for i in num:
    print(i)
