# 로그인 프로그램 작성
# 등록된 아이디 : flower , 패스워드 : 1234

ID = 'flower'
PSW = '1234'

id = input('아이디 입력 :')
psw = input('패스워드 입력 :')

if(id == ID and psw == PSW):
    print('로그인 성공!')
else:
    print('로그인 실패')