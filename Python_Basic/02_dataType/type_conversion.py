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
