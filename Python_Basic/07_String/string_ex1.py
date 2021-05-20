# email type을 체크

email = input('input email : ')
if(email.find('@') == -1 or
        email.find('.') == -1 or
        email.index('@') > email.index('.') or
        email.index('.') - email.index('@') < 2 or
        email.index('@') == 0 or
        len(email) - email.index('.') <= 1 or
        email.count('@') >= 2 or
        email.count('.') >= 2):
    print('이메일 형식이 아닙니다')
print('입력한 이메일 : %s' % email)