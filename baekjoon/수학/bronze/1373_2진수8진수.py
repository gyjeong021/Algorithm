# 문제 설명 : 2진수를 8진수로 변환
# 핵심 개념 : 진수 변환 내장 함수

binary = int(input(),2) # int(a,b) : b진수를 10진수로 변환, b의 default 10

octal = oct(binary)[2:] # oct() : 8진수 변환 함수
# bin() : 2진수 변환 함수, hex() : 16진수 변환 함수

print(octal)