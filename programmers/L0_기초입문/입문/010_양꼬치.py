# 양꼬치
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120830
# 알고리즘: 기초
# 작성자: 한규리
# 작성일: 2026. 02. 06. 19:07:14

def solution(n, k):
    service_drinks = n // 10
    answer = (n * 12000) + ((k - service_drinks) * 2000)    
    return answer