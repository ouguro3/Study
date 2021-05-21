
crawling = 'Data crawling is fun'


print(crawling.find('i'))
print(crawling.rfind('i'))
print(crawling.find('i', 1, 9))

print('----------------------')
print(crawling.index('i'))
print(crawling.rindex('i'))
print(crawling.index('i'))

# split() : 지정된 문자로 문자열을 분할함, 리스트 형식으로

token = crawling.split()
print(token)

names = 'Lee,Kim,Choi,Kang'
nameL = names.split(',') # ['Lee','Kim','Choi','kang']

for n in nameL:
    print(n)


for i in range(len(nameL)):
    print(nameL[i])


# 문자열의 요소 하나씩 출력력
for c in crawling:
    print(c)
