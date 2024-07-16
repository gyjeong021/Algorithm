# 알고리즘 분류 : 스택
# 문제 설명 : 후위 표기식 계산
# 핵심 개념 : 스택 사용, ord() : 문자의 아스키코드 값 반환

n = int(input())

sentence = input()
operand = [int(input()) for i in range(n)] # 피연산자 리스트 길이 지정

stack = []

for j in sentence :
    if 'A' <= j <= 'Z' :
        stack.append(operand[ord(j)-ord('A')]) # ord('A') = 65, A부터 차례대로 operand 값을 가지게 됨
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

print('%.2f' %stack[0]) # 소숫점 둘째자리까지 출력