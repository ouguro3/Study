# replace()

text = 'Java Programming'
b = text.replace('Java','Python')
print(b)

# 대문자/소문자 변환
# upper() : 대문자 변환    lower() : 소문자 변환
# capitalize() : 문단의 첫글자 대문자 변환   title() : 문장의 첫 글자만 대문자 변환

text = 'java programming is fun'
print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())

# 공백문자 제거 strip(), lstrip(), rstrip()

text = '         java programming is fun          '
print(text + '---')
print(text.strip())
print(text.lstrip())
print(text.rstrip() + '---')
