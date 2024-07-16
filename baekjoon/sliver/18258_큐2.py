# 알고리즘 분류 : 큐
# 문제 설명 : 큐 함수 명령을 처리하는 프로그램 작성
# 핵심 개념 : 큐 Queue - FirstinFirstOut(FIFO, 선입선출)

import sys
from collections import deque

n = int(input())
que = deque()

for _ in range(n) :
    x = sys.stdin.readline().split()
    if x[0] == "push":
        que.append(x[-1])
    elif x[0] == "pop" :
        if len(que) == 0 :
            print(-1)
        else :
            print(que.popleft())
    elif x[0] == "size" :
        print(len(que))
    elif x[0] == "empty" :
        if len(que) == 0 :
            print(1)
        else :
            print(0)
    elif x[0] == "front" :
        if len(que) == 0 :
            print(-1)
        else :
            print(que[0])
    elif x[0] == "back" :
        if len(que) == 0 :
            print(-1)
        else :
            print(que[-1])
 