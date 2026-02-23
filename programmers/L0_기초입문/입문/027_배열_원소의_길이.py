# 배열 원소의 길이
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120854
# 알고리즘: 기초
# 작성자: 한규리
# 작성일: 2026. 02. 23. 09:30:40

def solution(strlist):
    answer = []
    for s in strlist:
        answer.append(len(s))
    return answer