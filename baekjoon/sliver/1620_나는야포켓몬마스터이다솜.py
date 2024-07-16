# 알고리즘 분류 : 해시를 사용한 집합과 맵
# 문제 설명 : 포켓몬 번호와 이름에 해당하는 이름과 번호 출력
# 핵심 개념 : 번호와 이름을 저장하는 딕셔너리를 따로 만들기

import sys

n, m = map(int, input().split())

pokemon_num = {}
pokemon_name = {}

for i in range(1,n+1) :
    x = sys.stdin.readline().strip()
    pokemon_num[i] = x
    pokemon_name[x] = i

for _ in range(m) :
    problem = sys.stdin.readline().strip()
    if problem.isdigit() : # isdigit() : 숫자인지 판단
        print(pokemon_num[int(problem)])
    else :
        print(pokemon_name[problem])
