# 문제 설명 : 공백 없는 N개의 숫자들 합하기

# 방법 (1)
# 핵심 개념 : sum 함수, map 함수

num = input()

print(sum(map(int,input())))


# 방법 (2)
# 핵심 개념 : for 문
num = input()
numbers = input()
sum = 0

for i in numbers :
    sum += int(i)

print(sum)