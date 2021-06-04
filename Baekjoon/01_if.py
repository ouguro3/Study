# 문제 1

# 사분면 판별하기

# 두 정수를 입력받아 사분면중 어느쪽인지 판별

a = int(input())
b = int(input())
if a > 0 and b > 0:
    print('1')
elif a < 0 and b > 0:
    print('2')
elif a < 0 and b < 0:
    print('3')
else:
    print('4')