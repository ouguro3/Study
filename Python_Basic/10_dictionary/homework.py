# 1. 학생들의 이름과 성적을 딕셔너리로 저장하고 있다
# 각 학생의 총점과 평균을 계산하여 출력하시오

students = [
   {"name" : "홍길동", "korean" : 87, "math" : 98, "english" : 88, "science" : 95},
   {"name" : "이몽룡", "korean" : 92, "math" : 98, "english" : 96, "science" : 98},
   {"name" : "성춘향", "korean" : 76, "math" : 96, "english" : 94, "science" : 90},
   {"name" : "변학도", "korean" : 98, "math" : 92, "english" : 96, "science" : 92},
   {"name" : "박지성", "korean" : 95, "math" : 98, "english" : 98, "science" : 98},
   {"name" : "류현진", "korean" : 64, "math" : 88, "english" : 92, "science" : 92}
]
print('이름'.rjust(1), '총점'.rjust(6), '평균'.rjust(7))
for i in students:
    name = (i['name'])
    kor = (i['korean'])
    mat = (i['math'])
    eng = (i['english'])
    sci = (i['science'])
    total = kor + mat + eng + sci
    aver = total / 4
    print('%s'.ljust(4) % name,end='\t')
    print('%d'.rjust(3) % total,end='\t')
    print('%.1f'.rjust(5) % aver)


# 2. 딕셔너리를 이용하여 사용자로 부터 영어단어와 뜻을 입력받아 사전을 구성,
# 사용자가 입력한 단어를 검색하여 뜻을 출력하는 프로그램 작성

wor = []
mea = []

dic = dict()
while True:
    word = input('영어 단어 등록 (종료는 Quit) :')
    wor.append(word)
    if word in dic:
        print('%s는 이미 등록된 단어입니다' % word)
        continue
    elif word == 'Quit':
        break
    mean = input('%s의 뜻 입력 (종료는 Quit) :' % word)
    mea.append(mean)
    if mean == 'Quit':
        break
    dic = dict(zip(wor,mea))
    # print(dic)
while True:
    word2 = input('검색할 단어 입력 (종료는 Quit) :')
    if word2 in dic:
        word3 = dic.get(word2)
        print(word2,'의 뜻은', word3,'입니다')
    elif word2 == 'Quit':
        print('사전 종료')
        break
    elif word2 not in dic:
        print('사전에 없는 단어입니다')



