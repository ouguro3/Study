# 선형리스트의 일반 구현

katok = ['다현','정연','쯔위','사나','지효']

def insert_data(position, friend):
    katok.append(None)
    kLen = len(katok)

    for i in range(kLen-1,position, -1):
        katok[i] = katok[i-1]

    katok[position] = friend

insert_data(2,'솔라')
print(katok)

insert_data(6,'문별')
print(katok)