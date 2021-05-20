# 두 숫자를 입력받아서 이 수 사이의 숫자의 합을 구하기

a = int(input('첫번째 숫자 입력:'))
b = int(input('두번째 숫자 입력:'))

total = 0
for i in range(a,b+1):
    print(i,end=' ')
    total += i
print('\n===================')
print(total)

# 단 수를 입력받아 해당 구구단 출력
a = int(input('구구단 단수 입력:'))

for i in range(2,10):
    print(a,'X',i,'=',a*i)



# 카운트 다운 프로그램 작성
a = int(input('시작 숫자를 입력하세요 :'))
for i in range(a,0,-1):
    print(i,end=' ')
print('발사')