# 알고리즘 분류 : 문자열 & 스택

# 문제 설명 : <>로 감싸진 부분 제외한 단어들 뒤집기
# 핵심 개념 : stack - LIFO(last in first out, 후입선출), pop()

sentence = input() + " "

stack = []
result = ""
status = False # <> 안일 때 True, 밖일 때 False

for i in sentence :
    if i == "<" :
        status = True
        for _ in range(len(stack)) : # "<" 이전 단어 뒤집기
            result += stack.pop()

    stack.append(i)

    if i == ">" :
        status = False
        for _ in range(len(stack)) :
            result += stack.pop(0) # 0번째 원소 삭제

    if i == " " and status == False :
        stack.pop()
        for _ in range(len(stack)) :
            result += stack.pop()
        result += " "

print(result)

