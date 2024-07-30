# 알고리즘 분류 : 문자열
# 문제 설명 : 문자열이 규칙을 만족하는지 검사
# 핵심 개념 : 정규 표현식

import sys
import re

t = int(input())
pattern = re.compile('^[A-F]?A+F+C+[A-F]?$') # 정규 표현식 컴파일
# ^ : 해당 패턴으로 시작
# $ : 해당 패턴으로 끝
# ? : 해당 패턴 0~1번
# * : 해당 패턴 0번 혹은 그 이상
# + : 해당 패턴 1번 혹은 그 이상

for _ in range(t) :
    chromosome = sys.stdin.readline()
    if pattern.match(chromosome) == None :
        print("Good")
    else :
        print("Infected!")

# match() : 문자열 처음부터 정규식과 매치되는지 조사, 매치되지 않을 때 리턴 값 None
# search() : 문자열 전체를 검색해 정규식과 매치되는지 조사, 매치되지 않을 때 리턴 값 None
# findall() : 정규식과 매치되는 모든 문자열 리스트로 리턴
# finditer() : 정규식과 매치되는 모든 문자열을 반복 가능한 객체로 리턴