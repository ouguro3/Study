# 이름이 명단에 있는지 검색

names = ['홍길동','이몽룡','성춘향','변학도']

a = input('이름 입력 :')

for name in names:
    if a == name:
        flag = True
        break
    else:
        flag = False

if flag == True:
    print('명단에 있습니다')
else:
    print('명단에 없습니다')