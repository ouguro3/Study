# 생일 입력 (연/월/일) : 1998/9/20
# 당신은 1998년에 태어나셨군요
# 생일은 9월 20일 이네요
'''
birth = input('생일 입력 (연/월/일):')
a = birth.split('/')
print('당신은', a[0],'년에 태어나셨군요')
print('생일은', a[1],'월' ,a[2],'일 이네요')
'''

# 주어진 데이터에서 점수만 추출하여 숫자화 하고 총점과 평균을 구하시오

# split을 이용하여 분리
# 문자열.split(':')

# 첫번째 분리된 결과는 리스트 형태로 주어지므로 반복문 for 를 사용하여 다음 분리때 활용
# 리스트의 요소를 가져오려면 [] 사용

# data = '{a1:30},{a2:50},{a3:20},{a4:70},{a5:40}'
# data2 = data.split(',')
# sum = 0
# # print(data2)
# for i in range(len(data2)):
#     a,b = data2[i][1:-1].split(':')
#     # print(b)
#     sum += int(b)
# print('총점 :%d'%sum)
# avr = sum / len(data2)
# print('평균 :%.1f'%avr)

data = '{a1:30},{a2:50},{a3:20},{a4:70},{a5:40}'
data2 = data.split(',')
sum = 0
for i in range(len(data2)):
    # print(data2)
    a = data2[i][4:6]
    # print(a,end=' ')
    sum += int(a)
print('총점 :%d'%sum)
avr = sum / len(data2)
print('평균 :%.1f'%avr)