# OX 퀴즈

n = int(input())

count = 0
total = 0

for i in range(n):
    s = list(map(str,input()))
    for j in range(len(s)):
        if s[j] == 'o':
            count += 1
        elif s[j] == 'x':
            count == 0
    print(count)
    count = 0




