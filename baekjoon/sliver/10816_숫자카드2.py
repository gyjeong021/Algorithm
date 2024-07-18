# 알고리즘 분류 : 해시를 사용한 집합과 맵
# 문제 설명 : 상근이가 숫자 카드를 몇개 가지고 있는지 구하기

# 방법 (1)
# 핵심 개념 : 딕셔너리 사용

import sys

n = int(input())
card_n = list(map(int, sys.stdin.readline().split()))

cards = {}
for card in card_n :
    if card in cards :
        cards[card] += 1
    else :
        cards[card] = 1

m = int(input())
card_m = list(map(int, sys.stdin.readline().split()))

for i in card_m :
    result = cards.get(i)
    if result == None :
        print("0", end=" ")
    else :
        print(result, end=" ")


# 방법 (2)
# 핵심 개념 : 이분탐색

import sys

n = int(input())
card_n = sorted(list(map(int, sys.stdin.readline().split())))

cards = {}
for card in card_n :
    if card in cards :
        cards[card] += 1
    else :
        cards[card] = 1

m = int(input())
card_m = list(map(int, sys.stdin.readline().split()))

def binary_search(target, arr, start, end) :
    if start > end :
        return 0
   
    mid = (start + end) // 2
        
    if target == arr[mid] :
        return cards[target]
    elif target < arr[mid] :
        return binary_search(target, arr, start, mid-1)
    else :
        return binary_search(target, arr, mid+1, end)
    
for m in card_m :
    print(binary_search(m, card_n, 0, len(card_n)-1), end=" ")