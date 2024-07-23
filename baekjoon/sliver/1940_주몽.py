# 알고리즘 분류 : 투포인터
# 문제 설명 : 재료 N으로 몇개의 갑옷(M)을 만들 수 있을지 구하기
# 핵심 개념 : 투포인터

import sys

n = int(input())
m = int(input())
n_num = list(map(int, sys.stdin.readline().split()))

n_num.sort()
left = 0
right = len(n_num) - 1
count = 0

while left < right :
    sum = n_num[left] + n_num[right]
    if sum < m :
        left += 1
    elif sum > m :
        right -= 1
    else :
        count += 1
        left += 1
        right -= 1

print(count)
    

