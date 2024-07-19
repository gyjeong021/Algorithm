# 알고리즘 분류 : 덱
# 문제 설명 : 초기 카드 배치 상태 출력
# 핵심 개념 : deque appendleft() 사용

from collections import deque
import sys

n = int(input())
skill = list(map(int, sys.stdin.readline().split()))
skill.reverse()
initial = deque()

for i in range(n) :
    if skill[i] == 1 :
        initial.appendleft(i+1)
    elif skill[i] == 2 :
        initial.insert(1, i+1)
    else :
        initial.append(i+1)

for i in initial :
    print(i, end=" ")
    
'''
시간초과!
아래 반복문 보다 위의 리스트에 직접 접근하는 방법이 더 좋다
for i in range(n) :
    print(initial[i], end=" ")    
'''