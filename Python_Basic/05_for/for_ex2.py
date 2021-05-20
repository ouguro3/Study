# 1 에서 20까지의 정수 중 3의 배수 출력
total = 0
for i in range(3,21,3):
    print(i, end=' ')
    total += i
print('\n======')
print(total)

# 1-1 range 함수의 step 사용하지 않고 출력
total = 0
for i in range(1,21):
    if i % 3 == 0:
        print(i,end=' ')
        total += i
print('\n======')
print(total)