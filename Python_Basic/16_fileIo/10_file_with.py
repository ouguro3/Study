# with 문으로 파일 열기

# with open('test3.txt','w') as f:
#     f.write('hello')

filename = 'test4.txt'
data = '''나는 파이썬을 배우고 있어요
쉽지는 않지만
하나씩 내가 해내니 성취감이 느껴져 좋네요'''

with open(filename, 'w',encoding='utf-8') as f:
    f.write(data)
