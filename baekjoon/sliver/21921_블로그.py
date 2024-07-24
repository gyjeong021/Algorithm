# 알고리즘 분류 : 슬라이딩 윈도우
# 문제 설명 : X일 동안 가장 많이 들어온 방문자 수와 기간 구하기
# 핵심 개념 : 슬라이딩 윈도우 - 고정적인 길이의 배열 내 데이터를 이용하여 문제 풀이하는 알고리즘
# 배열 길이 고정적이기에 투 포인터와 달리 변수 하나만 있으면 됨

n, x = map(int, input().split())
visitor = list(map(int, input().split()))

sum = sum(visitor[:x])
max = sum
cnt = 1

for i in range(x,n) :
    sum -= visitor[i-x]
    sum += visitor[i]
    if max < sum :
        max = sum
        cnt = 1
    elif max == sum :
        cnt += 1

if max == 0 :
    print("SAD")
else :
    print(max)
    print(cnt)