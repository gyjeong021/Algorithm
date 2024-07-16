# 알고리즘 분류 : 스택
# 문제 설명 : '('와 ')'의 개수가 잘 매칭되어 구성되어있는지 확인
# 핵심 개념 : 스택 (후입선출)

n = int(input())

for _ in range(n) :
    stack = []
    sentence = input()
    for i in sentence :
        if i == "(" :
            stack.append(i)
        elif i == ")" :
            if len(stack) != 0 :
                stack.pop()
            else :
                print("NO")
                break
    else : # for 루프가 break 없이 끝까지 실행된 경우
        if len(stack) == 0 :
            print("YES")
        else :
            print("NO")