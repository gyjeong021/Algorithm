# 문제 설명 : 가장 빈도수가 높은 문자 출력
# 핵심 개념 : 자료형(딕셔너리, 리스트, 튜플), sorted 함수

num = int(input())

for i in range(num) :
    letter = dict() # letter의 자료형 : 딕셔너리
    sentence = input().rstrip() # rstrip() : 오른쪽 공백 제거
    sentence = sentence.replace(" ", "") # replace : 문자(열) 변경
    for j in sentence :
        if (j not in letter) :
            letter[j] = 1
        else :
            letter[j] += 1
    letter = sorted(letter.items(), key = lambda x:-x[1]) # letter의 자료형 : 튜플이 들어있는 리스트 
    # sorted : 새로운 정렬된 리스트 생성
    # lambda x:-x[1] : 튜플의 두번째 값을 가져와 내림차순 정렬
    
    if (len(letter)==1) :
        print(letter[0][0])
    elif (letter[0][1]==letter[1][1]) :
        print("?")
    else :
        print(letter[0][0])

