# 문제 설명 : 문장들을 세로로 읽어 출력
# 핵심 개념 : 이차원 배열

import sys

sentence = [["*" for i in range(15)] for j in range(5)]

for i in range(5):
    sentences = sys.stdin.readline().rstrip()
    for j in range(len(sentences)):
        sentence[i][j] = sentences[j]

for i in range(15):
    for j in range(5):
        if sentence[j][i] != "*":
            print(sentence[j][i], end="")

