# 리스트의 기본 개념

intL = [1,3,2,10]
floatL = [1.5, 3.2, 5.4]
nameL = ['홍길동','성춘향','변학도','방자']
numL = [1,3,4,[1,2]]
samL = [1,3,.5,'하하']

# print(intL)
# print(type(intL))
# print(numL)
# print(samL)
#
# for x in numL:
#     print(x)
#
# for i in range(len(numL)):
#     print(numL[i])
#
# a,b,c = floatL
# print(a)
# print(b)
# print(c)
#
# # 인덱싱
# print(nameL[-1])
# print(nameL[:])
# print(nameL[1:3])
# print(nameL[-1][0])

allL = [] # 빈 리스트 생성
allL = list()

allL = [intL,floatL,nameL,numL]
print(allL)
print(allL[-1][-1][0])

print(nameL[:-1])
print(nameL[-1:])
print(nameL[-1])
n = len(nameL)
print(nameL[:n])

# 리스트의 +, * 연산
sumL = numL + samL
print(sumL)
print(numL * 3)

# 리스트의 내용 변경
print(numL)
numL[3] = 10
print(numL)
numL[2:4] = []
print(numL)