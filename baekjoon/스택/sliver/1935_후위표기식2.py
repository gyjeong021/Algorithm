# 문제 설명 : 후위 표기식 계산
# 핵심 개념 : 스택 사용

## 오류!!
n = int(input())

sentence = input()
operand = [0]*n

for i in range(n) :
    operand[i] = int(input())

stack = []

for j in sentence :
    if 'A' <= j <= 'Z' :
        stack.append(operand[ord(i)-ord('A')])
    else :
        y = stack.pop()
        x = stack.pop()

        if j == '+' :
            stack.append(x + y)
        elif j == '-' :
            stack.append(x - y)
        elif j == '*' :
            stack.append(x * y)
        elif j == '/' :
            stack.append(x / y)

print('%.2f' %stack[0])