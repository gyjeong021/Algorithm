# 알고리즘 분류 : 스택
# 문제 설명 : 쇠막대기와 레이저의 배치를 나타내는 괄호 표현이 주어졌을 때, 레이저에 의해 잘려진 쇠막대기 조각의 총 개수를 구하기
# 핵심 개념 : 스택으

laser = input()
stack = []
cnt = 0

for i in range(len(laser)) :
    if laser[i] == "(" :
        stack.append("(")
    else :
        if laser[i-1] == "(" :
            stack.pop()
            cnt += len(stack)
        else :
            stack.pop()
            cnt += 1

print(cnt)