# 알고리즘 분류 : 수학
# 문제 설명 : 조합 계산 결과의 끝자리 0의 개수
# 핵심 개념 : 2와 5의 지수 개수를 구하기

n, m = map(int, input().split())

def count_two(n) :
    two_cnt = 0
    while n != 0 :
        n = n // 2 # 첫번째 : n/2, 두번째 : n/(2*2), 세번째 : n/(2*2*2) ...
        two_cnt += n
    return two_cnt

def count_five(n) :
    five_cnt = 0
    while n != 0 :
        n = n // 5 # 첫번째 : n/5, 두번째 : n/(5*5), 세번째 : n/(5*5*5) ...
        five_cnt += n
    return five_cnt

final_two = count_two(n) - count_two(m) - count_two(n-m)
final_five = count_five(n) - count_five(m) - count_five(n-m)

print(min(final_two, final_five))