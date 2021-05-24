# Q1. 홍길동씨의 평균 점수 구하기
kor = 80
eng = 75
mat = 55

total = kor + eng + mat
aver = total / 3
print('평균 점수 : %.1f'%aver) # 70.0

# Q2. 자연수 13이 홀수인지 짝수인지 판별할 수 있는 방법
a = 13
if a % 2 == 0:
    print('짝수입니다')
elif a % 2 != 0:
    print('홀수입니다')

# Q3. 홍길동씨의 주민번호는 881120-1068234 이다
# 연월일과 그 뒤의 숫자 부분으로 나누어 출력
# * 문자열 슬라이싱 기법 사용
a = '881120-1068234'
print(a[0:6])
print(a[7:])

# Q4. 주민등록번호 뒷자리의 맨 첫 번째 숫자는 성별을 나타낸다
# 성별을 나타내는 숫자를 출력
# * 문자열 인덱싱 기법 사용
a = '881120-1068234'
print(a[7])

# Q5. 문자열 a:b:c:d를 a#b#c#d 로 바꿔서 출력
a = 'a:b:c:d'
print(a.replace(':','#'))

# Q6. [1,3,5,4,2] 리스트를 내림차순 정렬 출력
a = [1,3,5,4,2]
a.sort(reverse=True)
print(a)

# Q7. ['Lift', 'is', 'too', 'short'] 리스트를 Life is too short 문자열로 만들기
# join() 함수를 이용하면 쉽다
a = ' '.join(['Life','is','too','short'])
print(a)

# Q8. (1,2,3) 튜플에 값 4를 추가하여 (1,2,3,4)를 만들자
a = (1,2,3)
b = (4,)
c = a + b
print(c)

# Q9. 다음중 오류나는것 찾고 설명
a = dict()
a['name'] = 'python'
a[('a',)] = 'python'
a[[1]] = 'python' ###  딕셔너리의 키에 리스트는 사용될 수 없다
a[250] = 'python'
print(a)

# Q10. 딕셔너리 a에서 'B'에 해당되는 값을 추출해 보자
a = {'A':90, 'B':80, 'C':70}
b = a.pop('B')
print(b)

# Q11. a리스트에서 중복 숫자를 제거
a = [1,1,1,2,2,3,3,3,4,4,5]
s1 = set(a)
l1 = list(s1)
print(l1)

# Q12. a,b 변수를 선언한 후 a의 요소값을 변경하면 b 값은?
# 이런 결과가 생기는 이유를 설명하라
a = b = [1,2,3]
a[1] = 4
print(b)
# a,b가 동일한 리스트를 가르키고 있다,  생성되는 id값이 동일