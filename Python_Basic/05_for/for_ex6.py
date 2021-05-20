# 다중 for문을 사용하여 다음과 같이 출력
# 1234
# 5678
# 9101112

'''
for i in range(3):
    for j in range(1,5):
        print(j+i*4,end='\t')
    print()
'''

a = 0
for i in range(3):
    for j in range(1,5):
        a += 1
        print(a, end='\t')
    print()