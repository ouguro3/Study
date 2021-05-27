# print(10/0)
# try:
#     print(10/0)
# except ZeroDivisionError as e:
#     print('오류가 발생',e)
# finally:
#     print('나누기')

# try:
#     print('age=' + 23)
# except Exception as e:
#     print(e)


# 여러개의 예외 처리 : 함께 처리 가능
# try:
#     print(10/0)
#     print('age=' + 23)
# except (ZeroDivisionError,Exception) as e:
#     print(e)

#
# try:
#     num = int(input('input number :'))
# except ValueError:
#     print('정수가 아닙니다')
# else:
#     print(num)
# finally:
#     print('종료')

try:
    f = open('testex.txt','r')
except FileNotFoundError:
    pass
else:
    data = f.read()
    print(data)
    f.close()
finally:
    print('종료')
