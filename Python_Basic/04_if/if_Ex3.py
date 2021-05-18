# 정수 3개를 입력받아서 제일 큰 수를 출력

a = int(input('정수 1 입력 :'))
b = int(input('정수 2 입력 :'))
c= int(input('정수 3 입력 :'))

if (a>b and a>c):
    max_num = a
elif (b>a and b>c):
    max_num = b
else:
    max_num = c

print('제일 큰 수는 %d 입니다'%max_num)