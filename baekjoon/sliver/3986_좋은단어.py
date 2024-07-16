# 알고리즘 분류 : 스택
# 문제 설명 : A와 B 각각이 짝을 이루어 선이 교차하지 않도록 매칭되는 개수 출력
# 핵심 개념 : 스택 (후입선출)

n = int(input())
cnt = 0

for _ in range(n) :
    stack = []
    sentence = input()
    for i in sentence :
        if len(stack) == 0 :
            stack.append(i)
        elif i == stack[-1] :
            stack.pop(-1)
        else :
            stack.append(i)

    if len(stack) == 0 :
        cnt += 1

print(cnt)

        