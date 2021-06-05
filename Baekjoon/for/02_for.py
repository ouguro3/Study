# 별 찍기

# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
# 첫째 줄에서 N을 입력받는다

n = int(input())
for i in range(n):
    for j in range(i+1):
        print('*',end='')
    print()

# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
# 첫째 줄에서 N을 입력받는다
# 단 오른쪽으로 정렬한다

n = int(input())
for i in range(n):
    for j in range(n-1,i,-1):
        print(' ',end='')
    for j in range(i+1):
        print('*',end='')
    print()

