# 모음 제거
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120849
# 알고리즘: 기초
# 작성자: 한규리
# 작성일: 2026. 02. 25. 09:33:56

def solution(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in vowels:
        my_string = my_string.replace(char, '')
    return my_string