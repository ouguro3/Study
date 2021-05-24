#

# 2차원 리스트
# list3 = [[1,2,3],[4,5,6],[7,8,9]]
# print(list3)
#
# for i in list3:
#     print(i)
#
# for i in list3:
#     for j in i:
#         print(j,end=' ')
#     print()
#
# # print(list3[1][1])
# print(len(list3))
# print(len(list3[0]))

# 연습문제

# 10명의 학생의 국어,영어,수학 점수가 2차원 리스트 형식으로 저장된 경우
# 각 학생별 세 과목의 총점과 평균 점수를 계산하여 과목 점수와 함께 출력하는 코드 작성
# 그냥 리스트 주니까 재미가 없어서 입력받아서 하는것으로 변경

a1 = []
for i in range(1,11):
    print('%d 번 학생' % i)
    kor = int(input('국어 :'))
    eng = int(input('영어 :'))
    math = int(input('수학 :'))
    i = []
    i.append(kor)
    i.append(eng)
    i.append(math)
    a1.append(i)

for i in a1:
    total = 0
    for j in i:
        total += j
    print('점수 :',i,'총점 :',total,'평균',total/len(i))




