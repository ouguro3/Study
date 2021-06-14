# 평균은 넘겠지

# 대학생 새내기의 90%는 자신이 반에서 평균은 넘는다고 생각한다
# 그게 사실이 아니라는것을 증명해보자

c = int(input())

for i in range(c):
    total = 0
    avr = 0
    f_avr = 0
    count = 0
    n = list(map(int,input().split()))
    for j in range(1,len(n)):
        total += n[j]
    avr = total / (len(n) - 1)
    for k in range(1,len(n)):
        if n[k] > avr:
            count += 1
        else:
            continue
    f_avr = count / (len(n) - 1) * 100
    print('%.3f%%'%f_avr)
