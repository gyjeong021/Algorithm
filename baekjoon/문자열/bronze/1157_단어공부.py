# 문제 설명 : 가장 많이 사용된 알파벳 출력

# 방법 (1)
# 핵심 개념 : set(집합)과 count 함수, index 함수

word = input().upper()
word_list = list(set(word)) # set은 중복 제거

cnt = []
for i in word_list :
    cnt.append(word.count(i)) # word.count(i) : word 안에 i의 개수 

if cnt.count(max(cnt)) > 1 :
    print("?")
else : 
    print(word_list[cnt.index(max(cnt))])


# 방법 (2)
# 핵심 개념 : 딕셔너리와 sorted 함수 (9046과 비슷한 방식의 풀이)

word = input().upper()

letter = dict()
for i in word :
    if i not in letter :
        letter[i] = 1
    else :
        letter[i] += 1

sorted_letters = letter = sorted(letter.items(), key = lambda x:-x[1])

if len(sorted_letters)==1 :
    print(sorted_letters[0][0])
elif sorted_letters[0][1]==sorted_letters[1][1] :
    print("?")
else :
    print(sorted_letters[0][0])
