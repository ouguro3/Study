# 키보드로부터 두 개의 정수를 입력을 받고,
# 두 수의 합과 평균을 구한 후 합과 평균을 출력하시오.
num1 = int(input('정수1 입력:'))
num2 = int(input('정수2 입력:'))

total = num1+num2
avg = total/2
# print('두 수의 합은 %d, 평균은 %.2f' %(total, avg))
# print('두 수의 합은 {0}, 평균은 {1}'.format(total, avg))

# print(format(total, '10.2f'))
print('두 수의 합은 {0:d}, 평균은 {1:9.2f}'.format(total, avg))
print('두 수의 평균 {1}, 합은 {0}'.format(total, avg))