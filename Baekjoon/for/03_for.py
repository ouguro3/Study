# X 보다 작은 수

# 첫번째 줄에서 N 과 X 가 주어진다
# 둘째줄에 수열 A를 이루는 정수 N 개가 주어진다
# X 보다 작은 수를 입력 받은 순서대로 공백으로 구분해 출력한다

# 1번 방법
N, X = map(int,input().split())
A = []
for i in range(N):
    num = int(input())
    A.append(num)
for i in A:
    if i < X:
        print(i,end=' ')

# 2번 방법
N, X = map(int,input().split())
A = list(map(int,input().split()))

for i in A:
    if i < X:
        print(i,end=' ')
