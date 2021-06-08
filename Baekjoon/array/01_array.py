# 숫자 세기

# 세개의 자연수 A,B,C 가 주어질 때 A x B x C 를 계산한 결과에
# 0부터 9까지의 숫자가 몇번 쓰였는지 출력하는 프로그램 작성

a = int(input())
b = int(input())
c = int(input())

total = a*b*c
total = str(total)
for i in range(10):
    print(total.count(str(i)))