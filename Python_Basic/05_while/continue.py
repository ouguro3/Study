# continue문
x = 0
while x < 10:
    x += 1
    if x % 2 == 0:
        continue
    print(x)

# 무한 반복(Loop) & break
while True:
    print('반복 시작')
    answer = input('종료하려면 x 입력 :')
    if answer == 'x':
        break

print('반복 종료')