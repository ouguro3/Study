# 알파벳 찾기

# 알파벳 소문자로만 이루어진 단어 S가 주어진다
# 각각의 알파벳에 대하여 단어에 포함되어 있는 경우는 위치를,
# 포함되어 있지않은 경우 -1을 출력하는 프로그램 작성

# 제출
from string import ascii_lowercase
alp = list(ascii_lowercase)
s = list(map(str, input()))
for i in alp:
    if i in s:
        print(s.index(i), end=' ')
    else:
        print(-1, end=' ')

# for i in range(97,123) >> 아스키 코드를 사용해 알파벳 소문자 출력하는법


