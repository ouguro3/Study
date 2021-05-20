# 숫자 10개 입력받아서 양,음,0의 개수 구하기

cnt1, cnt2, cnt3= 0

for i in range(1,11):
    a = int(input('숫자 %d 입력:'%i))
    if a > 0:
        cnt1 += 1
    elif a < 0:
        cnt2 += 1
    elif a == 0:
        cnt3 += 1
print('양의 개수: %d'%cnt1)
print('음의 개수: %d'%cnt2)
print('0의 개수: %d'%cnt3)

