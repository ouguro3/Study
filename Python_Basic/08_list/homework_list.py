# 1. 회원 이름을 입력받아 회원 명단 리스트를 생성하고, 회원 명단 리스트의 내용을 출력 (3명으로 제한)
names = []
for i in range(3):
    name = input('회원 이름 입력 :')
    names.append(name)
print('회원 명단 :', *names)

# print('===================================')
#
# 2. 학생 수를 입력받아 학생의 수만큼 점수를 입력받은 후 총점과 평균을 계산하고, 80점 이상인 학생의 수를 출력
scores = []
total = 0
high = 0
stu = int(input('학생 수 입력 :'))
for i in range(stu):
    score = int(input('학생 %d 점수 입력 :'%(i+1)))
    scores.append(score)
    total += score
    if score >= 80:
        high += 1

print('총점 : %d' % total)
aver = total / (len(scores))
print('평균 : %.1f' % aver)
print('80점 이상 학생 : %d' % high)

# print('===================================')

# 3. 상품을 리스트에 추가하고 엔터키를 누르면 입력이 종료되고 등록된 상품 리스트를 출력
prod = []
while True:
    n = input('상품 등록 (엔터키 누르면 종료) :')
    prod.append(n)
    if n == '':
        break
print('등록된 상품 :', *prod)



