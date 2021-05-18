# 입력한 정수 양수, 음수, 0 판별

num = int(input('정수 입력 :'))

# 1 그냥 if 문
if(num>0):
    print('양수')
else:
    if(num<0):
        print('음수')
    else:
        print('0')

# 2 elif 사용
if num>0:
    print('양수')
elif num<0:
    print('음수')
else:
    print('0')