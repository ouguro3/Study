# 평균

# 세준이는 기말고사를 망쳤다 그래서 점수를 조작하기로 했다
# 일단 자기 점수중 최댓값을 고르고 모든 점수를 점수/최대값 * 100으로 고쳤다
# 바뀐 점수로 새로운 평균을 구하시오

total = 0
n = int(input())
b = list(map(int,input().split()))
max_num = max(b)
for i in range(n):
    b[i] = b[i] / max_num * 100
for i in b:
    total += i
total /= n
print(total)
