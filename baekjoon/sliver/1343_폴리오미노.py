# 알고리즘 분류 : 그리디
# 문제 설명 : X로 채워진 보드판을 AAAA와 BB로 채우기
# 핵심 개념 : replace() 함수

board = input()

board = board.replace("XXXX", "AAAA")
board = board.replace("XX", "BB")

if "X" in board :
    print(-1)
else :
    print(board)