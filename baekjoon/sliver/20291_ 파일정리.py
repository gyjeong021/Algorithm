# 알고리즘 분류 : 문자열
# 문제 설명 : 확장자 파일의 개수 출력과 이름을 사전 순으로 출력
# 핵심 개념 : 딕셔너리 사용, 정렬

n = int(input())
file_num = dict()

for _ in range(n) :
    file = (input().split("."))[1]
    if file in file_num :
        file_num[file] += 1
    else :
        file_num[file] = 1

sorted_file_num = sorted(file_num.items()) # 키 값을 기준으로 정렬
# sorted_file_num = sorted(file_num.items(), key = lambda item:item[1]) value 값을 기준으로 오름차순 정렬
# sorted_file_num = sorted(file_num.items(), key = lambda item:item[1], reverse=True) value 값을 기준으로 내림차순 정렬

for key, value in sorted_file_num :
    print(key, value)
    