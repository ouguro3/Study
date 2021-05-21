# 문자열의 구성요소 판단
# isalpha() : 문자여부 True False
# isdigit() : 숫자여부
# isspace() : 공백 여부
# isalnum() : 영문과 숫자 여부
# islower() : 소문자 여부
# isupper() : 대문자 여부


# text = '1234567num'
# print(text.isdigit())
# print(text.isalpha())
# print(text.isalnum())
# print('    '.isspace())
# print('Abc'.islower())
# print('ABC'.isupper())
#
# print('a'.isdigit())
# print('1'.isalpha())
# print('A'.islower())
# print('A'.isupper())

# 연습문제. 문장을 입력하여 알파벳과 숫자, 스페이스, 그외 문자의 개수를 계산 출력
# ex) '나의 email 주소는 imlkm70@daum.net 입니다'

en = num = spa = tex = 0
text = input('문장을 입력하세요 :')
print(text)
for i in text:
    print(i)
    if i.encode().isalpha() == True:
        en += 1
    elif i.isdigit() == True:
        num += 1
    elif i.isspace() == True:
        spa += 1
    else:
        tex += 1
print('알파벳 개수 : {0} 숫자 개수 : {1} 공백 개수 : {2}  그외 문자 개수 : {3}'.format(en,num,spa,tex))