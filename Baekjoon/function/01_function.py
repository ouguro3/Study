# 정수 N개의 합

# 정수 n개가 주어졌을 때, n개의 합을 구하는 함수를 작성

def solve(a: list) -> int:
    sum = 0
    for i in a:
        sum += i
    return sum
total = solve([1,2,3,4])
print(total)