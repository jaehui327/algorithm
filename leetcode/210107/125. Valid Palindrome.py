#
# 125. Valid Palindrome
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# Note: For the purpose of this problem, we define empty string as valid palindrome.
#
# Example 1:
# Input: "A man, a plan, a canal: Panama"
# Output: true
#
# Example 2:
# Input: "race a car"
# Output: false
#
from collections import deque
import re


def is_palindrome(s: str) -> bool:  # 1. 리스트로 변환
    strs = []
    for char in s:
        if char.isalnum():  # 영문자, 숫자 여부 판별하여 해당하는 문자만 추가
            strs.append(char.lower())  # 소문자 변환
    # 팰린드롬 여부 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    return True


# O(n^2)
# 304ms


def is_palindrome2(s: str) -> bool:  # 2. 데크 자료형을 이용한 최적화
    # 자료형 데크로 선언
    strs = deque()
    for char in s:
        if char.isalnum():  # 영문자, 숫자 여부 판별하여 해당하는 문자만 추가
            strs.append(char.lower())  # 소문자 변환
    # 팰린드롬 여부 판별
    while len(strs) > 1:
        if strs.popleft() != strs.pop(): # 첫번째 요소를 가져올 때 popleft() -> O(1)
            return False

    return True


# O(n)
# 64ms

def is_palindrome3(s: str) -> bool:  # 3. 슬라이싱 사용
    s = s.lower()
    # 정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]  # 슬라이싱


# 36ms
