# 자료구조와 내장함수 연습문제

# 1. 실행결과 예측
mylist = ['apple','banana','grape']
result = list(enumerate(mylist))
print(result)

print('-'*40)

# 2. 실행결과 맞추기
cat_song = 'my cat has blue eyes, my cat is cute'
print({i:j for j,i in enumerate(cat_song.split())})

print('-'*40)

# 3. 실행결과 예측
colors = ['orange','pink','brown','black','white']
result = '&'.join(colors)
print(result)

print('-'*40)

# 4. 실행결과 맞추기
user_dict = {}
user_list = ['students','superuser','professor','employee']
for value_1, value_2 in enumerate(user_list):
    user_dict[value_2] = value_1
print(user_dict)

print('-'*40)

# 5. 실행결과 예측
result = [i for i in range(10) if i%2==0]
print(result)
items = 'zero one two three'.split('two')
result = [i for i in range(10)]
print(result)
items = 'zero one two three'.split()
print(items)
example = 'cs50.gachon.edu'
subdomain,domain, tld = example.split('.')
print(subdomain)

print('-'*40)

# 6. 실행결과 맞추기
animal = ['Fox','Dog','Cat','Monkey','Horse','Panda','Owl']
print([ani for ani in animal if 'o' not in ani])

print('-'*40)

# 7. 실행결과 맞추기
name = 'Hanbit University'
student = ['Hong','Gil','Dong']
split_name = name.split()
join_student = ''.join(student)
print(join_student[-4:] + split_name[1])

print('-'*40)

# 8. 실행결과 맞추기
kor_score = [49,79,20,100,80]
math_score = [43,59,85,30,90]
eng_score = [49,79,48,60,100]
midterm_score = [kor_score,math_score,eng_score]
print(midterm_score[0][2])

print('-'*40)

# 9. 실행결과 예측
a = [1,2,3]
b = [4,5,]
c = [7,8,9]
print([[sum(k), len(k)] for k in zip(a,b,c)])

print('-'*40)

# 10. 실행결과 맞추기
week = ['mon','tue','wed','thu','fri','sat','sun']
rainbow = ['red','orange','yellow','green','blue','navy','purple']
list_data = [week,rainbow]
print(list_data[1][2])

print('-'*40)

# 11. 실행결과 맞추기
# 72

print('-'*40)

# 12. 실행결과 맞추기
alist = ['a','b','c']
blist = ['1','2','3']
abcd = []

for a,b in enumerate(zip(alist,blist)):
    try:
        abcd.append(b[a])
    except IndexError:
        abcd.append('error')
print(abcd)

print('-'*40)

13.
alist = ['a1','a2','a3']
blist = ['b1','b2','b3']

for a,b in zip(alist,blist):
    print(a,b)

print('-'*40)


# 14. 실행결과 맞추기
alphabet = ["a","b","c","d","e","f","g","h"]
nums = [i for i in range(20)]
answer = [alpha+str(num) for alpha in alphabet for num in nums if num%2==0]
print(len(answer))