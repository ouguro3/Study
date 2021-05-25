# 함수의 반환값(return)

# def sum():
#     a = int(input('숫자 1 입력 :'))
#     b = int(input('숫자 2 입력 :'))
#     return a+b

# res = sum()
# print('합은 %d'%res)
# print('합은 %d'%sum())

# 삼각형의 넓이 계산 함수 get_triangle_area()
# 높이와 밑변을 키보드로 입력
# 결과값을 반환
# 높이 :
# 밑변 :
# 삼각형의 면적 :

# def get_triangle_area():
#     a = int(input('높이 :'))
#     b = int(input('밑변 :'))
#     tri = ('삼각형의 면적 : %d'%(a * b / 2))
#     return tri
#
# print(get_triangle_area())

# def get_triangle_area():
#     h = int(input('높이 : '))
#     w = int(input('밑변 : '))
#     area = h * w / 2
#     return h,w, area
#
# area = get_triangle_area()
# print('높이 %d, 밑변 %d, 삼각형의 넓이 % .2f'%(area[0],area[1],area[2]))

# def multiReturn():
#     return 1
#     return 2
#     return 3
#
# print(multiReturn())

# def order():
#     pri = int(input('상품가격 입력 :'))
#     num = int(input('주문수량 입력 :'))
#     total = pri * num
#     return pri, num, total
#
#
# price = order()
# print('-----------------')
# print('상품가격 : %d원\n주문수량 : %d개\n주문액 :%d원'%(price[0],price[1],price[2]))

# 리스트 반환값

# def getNames():
#     names = []
#     for i in range(3):
#         name = input('이름 입력 : ')
#         names.append(name)
#
#     return names
#
# nameL = getNames()
# print(nameL)

# 이름과 나이를 입력받아서 딕셔너리 형식으로 반환
# {'name':'홍길동','age':'20'}

def dict():
    dic = {}
    name = input('이름 입력 :')
    age = input('나이 입력 :')
    # dic['name'] = name
    # dic['age'] = age
    dic = {'name':name, 'age':age}
    return dic

diction = dict()
print(diction)
print(type(diction))

for key,value in diction.items():
    print(key,':',value)

for key in diction.keys():
    print(key,':',diction[key])