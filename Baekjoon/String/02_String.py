# 숫자의 합

# N개의 숫자가 공백없이 쓰여있다.
# 이 숫자를 모두 합해서 출력하는 프로그램을 작성

n = int(input())
plus = 0
num = list(map(int, input()))
for i in range(n):
    plus += num[i]
print(plus)
