# 알고리즘 분류 : 덱
# 문제 설명 : 제일 위 카드 버리고 다음 위에 있는 카드 밑으로 넣고를 반복하여 제일 마지막에 남는 카드 번호 출력
# 핵심 개념 : 큐 ( pop(0) - O(N) )을 사용하면 시간 초과, deque( popleft() - O(1) )를 사용하여 해결

from collections import deque

card_num = int(input())
card = deque([i+1 for i in range(card_num)])

while len(card) > 1 :
    card.popleft()
    x = card.popleft()
    card.append(x)

print(card[0])

