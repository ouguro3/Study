# 진수 변환 함수

# 2진수로 변환
print('2진수로 변환')
print(bin(11))
print(bin(0o11))
print(bin(0x11))

# 8진수로 변환
print('8진수로 변환')
print(oct(11))
print(oct(0b11))
print(oct(0x11))

# 16진수로 변환
print('16진수로 변환')
print(hex(11))
print(hex(0b11))
print(hex(0o11))

# int() 함수를 이용한 진수 변환
print(int('ff', 16))
print(int('123', 10))
print(int('123', 8))
print(int('1010', 2))