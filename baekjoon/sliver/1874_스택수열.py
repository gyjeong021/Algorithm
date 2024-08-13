# 알고리즘 분류 : 스택
# 문제 설명 : 입력된 수열을 만들기 위한 스택 연산 구하기
# 핵심 개념 : 스택

count = 1
flag = True
stack = []
answer = []

n = int(input())
for i in range(n):
    num = int(input())
    while count <= num:
        stack.append(count)
        answer.append('+')
        count += 1

    if stack[-1] == num:
        stack.pop()
        answer.append('-')

    else:
        flag = False
        break

if flag == False:
    print("NO")
else:
    for i in answer:
        print(i)