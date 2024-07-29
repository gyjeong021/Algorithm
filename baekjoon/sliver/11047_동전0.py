# 알고리즘 분류 : 그리디
# 문제 설명 : 동전의 합을 k로 만들 때 필요한 동전 개수의 최솟값 구하기
# 핵심 개념 : 그리디 알고리즘

import sys

n, k = map(int,input().split())
coins = []

for _ in range(n) :
    coins.append(sys.stdin.readline().strip())

coins.reverse()

count = 0

for coin in coins :
    if k >= int(coin) :
        count += k // int(coin)
        k = k % int(coin)

print(count)