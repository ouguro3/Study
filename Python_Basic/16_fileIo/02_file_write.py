# 파일에 쓰기 : 파일을 쓰기 모드(w)로 열고, 파일 객체의 write() 함수를 이용하여 파일에 출력

# data = 'hello'
# f = open('file2.txt','w') # 파일 객체
# f.write(data)
# f.close()


# data = '안녕하세요'
# f = open('file2.txt','w')
# f.write(data)
# f.close()
# 한글이 깨져보임

# 한글 인코딩 utf-8 지정
data = '안녕하세요'
f = open('text\\file2.txt','w',encoding='utf-8')
f.write(data)
f.close()
# utf-8 형식으로 저장 : 한글이 안깨짐

