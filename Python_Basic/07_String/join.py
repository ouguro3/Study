# join()

a = 'aa'
print(a.join('bbb')) # baabaab

b = '-'
print(b.join('1234')) # 1-2-3-4

numbers = ['10','20','30','40','50']
sep = ','
result = sep.join(numbers) # 10,20,30,40,50
print(result)

date = ['1990','01','01']
sep ='-'
print(sep.join(date))