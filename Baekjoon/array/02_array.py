# 나머지

# 수 10개를 입력받은 뒤, 이를 42로 나눈 숫자를 구하고,
# 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램 작성

lis = []
for i in range(10):
    n = int(input())
    n %= 42
    if n in lis:
        continue
    else:
        lis.append(n)
print(len(lis))
