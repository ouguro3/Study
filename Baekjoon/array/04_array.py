# OX 퀴즈

# OOXXOXXOOO 와 같은 OX 퀴즈의 결과가 있다.
# O는 문제를 맞은것이고,  X는 틀린것이다
# 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다
# ex) OOXXOXXOOO = 1+2+0+0+1+0+0+1+2+3 = 10
# OX 퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성

n = int(input())
for i in range(n):
    s = list(map(str,input()))
    count = 0
    total = 0
    for j in range(len(s)):
        if s[j] == 'O':
            count += 1
            total += count
        elif s[j] == 'X':
            count = 0
    print(total)





