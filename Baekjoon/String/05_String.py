# 단어 공부

# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성

s = input().lower()
s_l = list(set(s))
cnt = []

for i in s_l:
    count = s.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) >= 2:
    print('?')
else:
    print(s_l[(cnt.index(max(cnt)))].upper())















