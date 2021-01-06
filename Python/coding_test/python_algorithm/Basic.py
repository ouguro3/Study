# 인덴트(Indent)
# 파이썬의 대표적인 특징이기도 한 인덴트는 공식 가이드인 PEP 8에 따라 공백 4칸을 원칙으로 한다.

foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# 이 코드 처럼 첫 번째 줄에 파라미터가 있다면 파라미터가 시작되는 부분에 맞춰준다.

def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# 이 코드 처럼 첫 번째 줄에 파라미터가 없다면, 공백 4칸 인덴트를 한 번 더 추가하여 다른 행과 구별한다.

foo = long_function_name(
    var_one, var_two,
    var_three, var_four)

# 이 코드처럼 여러 줄로 나눠쓸 경우 다음 행과 구분되도록 인덴트를 추가한다.


# 네이밍 컨벤션(Naming Convention)

# 타입 힌트

# 리스트 컴프리헨션

# 제너레이터

# Range

# Enumerate

# // 나눗셈 연산자

# print

# pass

# locals