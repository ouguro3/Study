katok = ['다현','정연','쯔위','사나','지효']

# 함수 선언 부분

def add_data(friend):
    katok.append(None)
    kLen = len(katok)
    katok[kLen-1] = friend

def insert_data(position, friend):
    katok.append(None)
    kLen = len(katok)

    for i in range(kLen-1,position, -1):
        katok[i] = katok[i-1]

    katok[position] = friend

def delete_data(position):
    kLen = len(katok)
    katok[position] = None

    for i in range(position+1,kLen,1):
        katok[i-1] = katok[i]
        katok[i] = None

    del (katok[kLen-1])

## 전역 변수 선언 부분

katok = []
select = -1 # 1.추가 2.삽입 3.삭제 4.종료

if __name__ == '__main__':
    while (select != 4):
        select = int(input('1.추가 2.삽입 3.삭제 4.종료 >>'))
        if select == 1:
            data = input('추가할 데이터 >>')
            add_data(data)
            print(katok)
        elif select == 2:
            loc = int(input('삽입할 위치 >>'))
            data = input('삽입할 데이터 >>')
            if loc <= len(katok):
                insert_data(loc,data)
                print(katok)
            else:
                print('범위를 벗어났습니다')
                continue
        elif select == 3:
            loc = int(input('삭제할 데이터의 위치 >>'))
            if loc <= len(katok):
                delete_data(loc)
                print(katok)
            else:
                print('범위를 벗어났습니다')
                continue
        elif select == 4:
            print(katok)
            print('종료합니다')
            break
        else:
            print('1 ~ 4 중 하나를 입력해주세요')
            continue