# 타입 변환
# str(): 함수 : 숫자를 문자열로 변환
# print('나는 현재 나이가 ' + str(23) + '살 입니다')

# int() :정수 형식의 문자열을 정수로 변환
num = input('숫자를 입력하세요 :') # 키보드로 입력받은 자료를 num 변수에 할당
# print(type(num))
print(int(num) + 100)

print(int('123', 8)) # 8진수 0o123 # 2진수 : 1010011
print(int('123', 16)) # 16진수
print(int('1111', 2)) # 2진수

# float(문자열) : 문자열을 실수로 변환
print(float(num) + 100)

# 두개의 숫자(정수)를 입력받고 합과 평균을 구하시오
a = int(input('첫번째 숫자를 입력하세요 :'))
b = int(input('두번째 숫자를 입력하세요 :'))

total = a+b
aver = total / 2

print('두 수의 합은', total, '입니다')
print('두 수의 평균은', aver, '입니다')

# 포맷 이용
print('두 수의 합은 {0}, 평균은 {1} 입니다'.format(total,aver))