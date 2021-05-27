# 파일 내에서 검색
# seek(offset, whence) 함수

print('----- 파일 내에서 검색 seek() -----')
# f = open('test2.txt','r')
# f.seek(0,0) # 시작위치 0행 , 0열
# lines = f.readlines()
# print(lines)
# f.close

f = open('test2.txt','r')
# f.seek(1,0) # 시작위치 0행 , 1열
# f.seek(7,0) # 시작위치 0행 , 7열
# f.seek(14,0) # 시작위치 0행 , 14열
# f.seek(15,0) # 시작위치 0행 , 15열

lines = f.readlines()
print(lines)
f.close