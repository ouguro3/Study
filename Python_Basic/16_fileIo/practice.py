
# 파일 생성 및 내용 쓰기
# line = '''1 3
# 1 4
# 3 5
# 6 7
# 32 45
# 67 -32
# -13 45
# '''
# f = open('text\\practice.txt','w',encoding='utf-8')
# f.write(line)

# 파일 불러오기
# f = open('text\\practice.txt','r',encoding='utf-8')
# a = f.read()
# print(a)

# 데이터 여러줄 쓰기
# f = open('text\\practice.txt','w',encoding='utf-8')
# for i in range(5):
#     data = '%d행\n' % (i+1)
#     f.write(data)
# f.close()

# 여러줄 읽기
f = open('text\\practice.txt','r',encoding='utf-8')
# line = f.readline()
# print(line)
# line = f.readline()
# print(line)
lines = f.readlines()
for i in lines:
    print(i)