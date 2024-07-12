# 문제 설명 : 편집기의 명령어를 사용하여 작성된 최종 문자열을 구하기
# 핵심 개념 : 스택 2개 사용하기

import sys

# 커서 기준 왼쪽 : left, 오른쪽 : right
left = list(input())
n = int(input())
right = []

for _ in range(n) :
    edit = sys.stdin.readline().split()

    if edit[0] == "L" and left : # left에 단어가 있는 경우, 즉 커서가 맨 앞이 아닌 경우
        right.append(left.pop())
    elif edit[0] == "D" and right :
        left.append(right.pop())
    elif edit[0] == "B" and left : 
        left.pop()
    elif edit [0] == "P" :
        left.append(edit[1])

left = left + right[::-1] # right 리스트 reverse
print("".join(left)) # 리스트 대괄호 없이 출력 (반복문 사용 X)

# 시간 초과 (시간 제한 0.3초)
import sys

sentence = list(input())
n = int(input())
curser = len(sentence)

for _ in range(n) :
    edit = sys.stdin.readline().split()

    if edit[0] == "L" and curser > 0 :
        curser -= 1
    elif edit[0] == "D" and curser < len(sentence) :
        curser += 1
    elif edit[0] == "B" and curser > 0 : 
        sentence.pop(curser-1)
        curser -= 1
    elif edit [0] == "P" :
        sentence.insert(curser, edit[1])
        curser += 1

for i in sentence :
    print(i, end="")