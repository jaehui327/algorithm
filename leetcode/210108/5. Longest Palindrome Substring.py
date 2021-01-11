#
# 5. Longest Palindrome Substring
#
# Given a string s, return the longest palindromic substring in s.
#
# Example 1:
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#
# Example 2:
# Input: s = "cbbd"
# Output: "bb"
#
# Example 3:
# Input: s = "a"
# Output: "a"
#
# Example 4:
# Input: s = "ac"
# Output: "a"
#


def longest_palindrome(s: str) -> str:  # 중앙을 중심으로 확장하는 풀이
    # 팰린드롬 판별 및 투 포인터 확장
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    # 해당 사항이 없을 때 빠르게 리턴
    if len(s) < 2 or s == s[::-1]:
        return s
    result = ''
    # 슬라이딩 윈도우 우측으로 이동
    for i in range(len(s) - 1):
        result = max(result,
                     expand(i, i + 1),
                     expand(i, i + 2),
                     key=len)
    return result
