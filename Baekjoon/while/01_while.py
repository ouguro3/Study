# 더하기 사이클

# 입력된 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다.
# 입력된 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다
# 예) 26 -> 2+6 = 8  -> 새로운 수 68 -> 6 + 8 = 14 -> 새로운 수 84 -> 8 + 4 = 12
# 입력된 수가 몇번의 사이클만에 원래의 수와 같아지는지 구하는 프로그램 작성

n = int(input())
cnt = 0
m = n
while True:
    if m < 10:
        m1 = m*11
    n2 = m // 10
    n3 = m % 10
    n4 = (n2+n3) % 10
    n5 = n3*10 + n4
    cnt += 1
    if n5 == n:
        break
    m = n5
print(cnt)
