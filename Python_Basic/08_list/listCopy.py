# 리스트의 복사

# 얕은 복사

scores = [65, 70, 90, 89, 78]
value = scores

# print('scores :', scores)
# print('scores :', value)
#
# scores[3] = 98
# print('scores 값 변경 :', scores)
# print('value :', value)
#
# value[0] = 100
# print('scores :', scores)
# print('value :',value)

# 깊은 복사(deep copy) : copy(), list(), deepcopy()

# value2 = scores.copy()
# print('value2', value2)
# scores[0] = 50
# print('scores :', scores)
# print('value :', value)
# print('value2', value2)

value3 = list(scores)
print('value3 :',value3)
print('scores :', scores)
scores[0] = 150
print('scores :', scores)
print('value3 :', value3)

import copy

value4 = copy.deepcopy(scores)
scores[2] = 300
print('scores :', scores)
print('value4 :', value4)

