# append mode를 사용하여 파일끝에 추가
#
# f = open('test2.txt','a')
#
# data = '\n\n python programming'
# f.write(data)
# f.close

# 읽기모드로 파일을 열어서 내용 출력
f = open('test2.txt','a')

data = '\nR programming\n'
f.write(data)

f = open('test2.txt','r')
print(f.read())
f.close
