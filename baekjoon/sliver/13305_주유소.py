# 알고리즘 분류 : 그리디
# 문제 설명 : 도시를 이동하는데 드는 최소 주유 비용을 계산
# 핵심 개념 : 그리디 알고리즘 - 현재 상황에서의 최선을 선택하는 알고리즘
# 현재의 최선의 선택이 미래의 선택에 영향을 주지 않고 독립적

import sys

city = int(input())
road_len = list(map(int, sys.stdin.readline().split()))
oil_price = list(map(int, sys.stdin.readline().split()))

total_len = road_len[0] * oil_price[0] # 다음 도시까지의 도로 길이에 대해서만 주유
min_price = oil_price[0]

for i in range(1, city-1) :
    if min_price > oil_price[i] : # 더 싼 주유소 찾기
        min_price = oil_price[i]
    total_len += min_price * road_len[i] 

print(total_len)
