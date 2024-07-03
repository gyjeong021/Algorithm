# 문제 설명 : 두 자연수의 최대 공약수와 최소 공배수 출력

# 방법 (1)
# 핵심 개념 : 유클리드 호제법
# x와 y의 최대공약수는 y와 x%y의 최대공약수
# x와 y의 최소공배수는 x*y를 x와 y의 최대공약수로 나눈 값

x, y = map(int,input().split())

def gcd(x, y) : # 최대공약수
    while y > 0 :
        x, y = y, x % y
    return x

def lcm(x, y) : # 최소공배수
    return x * y // gcd(x, y)

print(gcd(x, y))
print(lcm(x, y))


# 방법 (2)
# 핵심 개념 : math 함수
import math

x, y = map(int,input().split())

print(math.gcd(x, y)) # 최대공약수
print(math.lcm(x, y)) # 최소공배수