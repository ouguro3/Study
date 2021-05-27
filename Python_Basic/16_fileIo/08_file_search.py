# read() 함수 이용하여 원하는 내용이 파일에 있는지 검색

value = input('검색 값 입력 : ')
f = open('test2.txt','r')
data = f.read()
if value in data:
    print('검색하려는 내용이 있습니다')
else:
    print('그런 내용이 없네요')

f.close()