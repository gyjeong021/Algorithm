# 문제 설명 : 패턴과 일치하는 문자열 찾기
# 핵심 개념 : input().split(), 리스트 슬라이싱

num = int(input())
front, back = input().split("*")
frontlen = len(front)
backlen = len(back)

for i in range(num) :
    file = input()
    if len(file) < frontlen + backlen :
        print("NE")
    elif file[:frontlen] == front and file[-backlen:] == back :
        # file[:frontlen] : 처음(0번째)부터 frontlen-1번째까지
        # file[-backlen:] : -backlen번째부터 끝까지, 뒤에서 backlen개 
        print("DA")
    else :
        print("NE")
