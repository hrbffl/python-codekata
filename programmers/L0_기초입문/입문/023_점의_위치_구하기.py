# 점의 위치 구하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120841
# 알고리즘: 기초
# 작성자: 한규리
# 작성일: 2026. 02. 13. 09:47:40

def solution(dot):
    x, y = dot[0], dot[1]
    
    if x > 0:
        return 1 if y > 0 else 4
    else:
        return 2 if y > 0 else 3