# 파일 읽어오기
# readline() : 1개의 행 씩 읽어오기, 행 끝에 '\n' 포함
# readlines() : 모든 행을 읽어 라인 단위별로 잘라서 리스트를 생성
#               ['...\n','...\n','...\n']
# read() : 내용 전체를 한 문자열로 반환 ''' '''

# 파일 전체 읽기
# f = open('test.txt','r')
# line = f.readlines()
# print(line)
# f.close()

# -- 파일 전체 읽고 각 행을 리스트에 저장하기 ---
# print('----- 파일 전체 읽기 -----')
# f = open('test.txt','r')
# myL = []
# while True:
#     line = f.readline()
#     if (line ==''):
#         break
#     myL.append(line)
# f.close()
# print(myL)

# readlines()로 읽은 내용을 한 줄씩 출력하기
f = open('test.txt','r')
lines = f.readlines()
for i in lines:
    print(i,end='')
f.close()