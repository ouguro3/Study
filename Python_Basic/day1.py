# # 첫번째 프로그램
#
# # print('Lee Hyun Bum")
#
# # 변수에 값을 저장(할당 assign)
# x = 10
# y = 20
# z = 30
# print(x,y,z)
#
# # 여러개의 변수에 여러개의 값을 저장
# x,y,z = 10,20,30
# print(x,y,z)
#
# # 여러 개의 변에 동일한 값을 할당
# a=b=c=100
# print(a,b,c)
#
# # 두 변수의 값을 교환(swap)
# a,b = 10,20
# print('a =',a)
# print('b =',b)
#
# print('[swap]')
#
# # 변수를 하나 더 지정하는 방법
# c = a
# a = b
# b = c
#
# # 파이썬의 swap 기능
# a,b = b,a
# print('a =',a)
# print('b =',b)
#
# # 변수를 삭제
# x = 100
# del x
# print(x)
#
# # 문자열에 큰 따옴표 사용
# name = '이현범'
# age = 32
# print(name,age)
#
# address = '경기도 평택시'
# print(name + '은' + address + '에 삽니다' )
#
# # str() : 숫자형을 문자열로 변환
# print(name + '은' + str(age) + '살 입니다')
# # + 를 사용할 때 문자열과 정수형 변수는 함께 사용이 불가능
#
# # 형변환
# # 값의 형태를 강제적으로 다른 형태로 변환하는 것
# # 예) int -> str, str-> float
# # 문자열 형변환 함수 str()
# # 정수형 형변환 함수 str()
# # 실수형 형변환 함수 str()
# ## 파이썬은 파일단위로 일괄 실행 시킨다.  가급적 콘솔 실행은 하지 말 것
#
# # 사각형의 면적을 구하는 프로그램
#
# width = 100
# height = 50
# area = width * height
# print('사각형의 면적은', area)
#
# # 실습 1.
# name = '이현범'
# no = 2016001
# year = 4
# grade = 'A'
# average = 93.5
#
# print('성명 : %s' % name)
# print('학번 : %d' % no)
# print('학년 : %d' % year)
# print('성적 : %s' % grade)
# print('평균 : %.1f' % average)
#
# print('이름: %s, 학년: %d'%(name,year))
# rate = 80
# print('이름: %s, 출석률: %d'%(name,rate))

# 실습 2.
kor,eng,math = 90,80,80
total = kor+eng+math
aver = total / 3

print('총점 :{:d}, 평균 :{:.1f}'%(total,aver))

