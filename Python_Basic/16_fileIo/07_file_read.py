# read() : 파일 전체를 읽어서 문자열 반환

f = open('test2.txt','r')
data = f.read()
print(data)
print(type(data))
print(len(data))

for ch in data:
    print(ch)

f.close()