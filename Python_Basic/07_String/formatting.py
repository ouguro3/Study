# formatting : %d  %f  %s  %c


# alphas = 20; digit = 30
# height = 179.33
# string = 'Python'
# print('문자 : %d 개'%alphas)
# print('문자 : ',format(alphas, 'd'),'개')
# print('문자 : {0}개, 숫자: {1}개'.format(alphas,digit))
# print('문자 : {alp}개, 숫자 : {dig}개'.format(alp=alphas,dig=digit))
# print('키는 {0:5.1f}'.format(height))
# print('{0:<10}'.format(string)) # 왼쪽 정렬
# print('{0:>10}'.format(string)) # 오른쪽 정렬
# print('{0:^10}'.format(string)) # 가운데 정렬
# print(string.ljust(10))  # 왼쪽 정렬
# print(string.rjust(10))  # 오른쪽 정렬
# print(string.center(10)) # 가운데 정렬

# 날짜 시간 출력 포맷
from datetime import date, datetime, timedelta

today = date.today()
print(today.year)
print(today.month)
print(today.day)

cur_time = datetime.now().time()
print(cur_time)
print(cur_time.hour)
print(cur_time.minute)
print(cur_time.second)
print(cur_time.microsecond)

cur_time = datetime.now()
print(today + timedelta(days=-1)) # 오늘 기준 하루 전
print(today + timedelta(days=7)) # 오늘 기준 7일 뒤
print(cur_time + timedelta(days=1, hours=2)) # 2021-05-22 15:32:20.536128

print(today.strftime('%Y-%m-%d %H:%M:%S')) # 2021-05-21 00:00:00