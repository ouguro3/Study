# 문자열의 기본 형식과 이해

crawling = 'Data crawling is fun.'
parsing = 'Data parsing is also'
'''
print(crawling)
print(parsing)

print(type(crawling))
print(type(parsing))

PI = 3.1415
r = 10

result = '반지름'+ str(PI) +  '인 원의 넓이는' + str(PI*r*r)
print(result)
'''

# slicing : 문자열 추출
print(crawling[0])
print(crawling[-1])
print(crawling[1:5])
print(crawling[:-1])
print(crawling[-1:]) # 마지막 문자
print(crawling[:])   # 문자열 전체
print(crawling[0:10])