# 파일에 쓰기 w : write()

# 여러 줄 데이터 쓰기
# f = open('file3.txt','w',encoding='utf-8')
# for i in range(1,11):
#     data = '%d행\n' % i
#     f.write(data)
# f.close()

# 파일 내용 : 1행2행3행4행5행6행7행8행9행10행

# f = open('file3.txt','w',encoding='utf-8')
# for i in range(1,11):
#     data = '%d행\n' % i
#     f.write(data)
# f.close()

# 파일 내용 : 줄바꿈되어 세로로 출력

# f = open('file3.txt','w',encoding='utf-8')
# for i in range(1,11):
#     data = '%d행\t' % i
#     f.write(data)
# f.close()

# 파일 내용 : 가로로 출력 1행	2행	3행	4행	5행	6행	7행	8행	9행	10행

f = open('file3.txt','w',encoding='utf-8')
for i in range(1,11):
    data = '%d행,' % i
    f.write(data)
f.close()

# 파일 내용 : 1행,2행,3행,4행,5행,6행,7행,8행,9행,10행,


