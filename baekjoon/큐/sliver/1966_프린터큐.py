# 문제 설명 : 중요도 높은 순으로 인쇄되는 프린터에서 몇번째로 인쇄되는지 출력 
# 핵심 개념 : deque 사용, popleft(), map()

from collections import deque

n = int(input())

for _ in range(n) :
    x, y = map(int, input().split())
    file = deque(list(map(int, input().split())))
    cnt = 0

    while file :
        big = max(file)
        now = file.popleft()

        if big == now :
            cnt += 1
            if y == 0 :
                print(cnt)
                break
            else :
                y -= 1
        else :
            file.append(now)
            if y == 0 :
                y = len(file)-1
            else :
                y -= 1
        
