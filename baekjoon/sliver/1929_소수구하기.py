# 알고리즘 분류 : 수학
# 문제 설명 : 소수 출력
# 핵심 개념 : 에라토스테니스의 체 (제곱근을 이용)

m, n = map(int, input().split())

for i in range(m, n+1) :
    if i == 1 :
        continue
    for j in range(2, int(i**0.5)+1) :
        if i % j == 0 :
            break
    else :
        print(i)

## 시간 초과 !
m, n = map(int, input().split())
list = []

for i in range(m, n+1) :
    status = True
    if i == 1 :
        continue
    for j in range(2, i) :
        if i % j == 0 :
            status = False
            break
    if status :
        list.append(i)

for i in list :
    print(i)

        
        