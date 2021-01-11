#
# 344. Reverse String
#
# Write a function that reverses a string. The input string is given as an array of characters char[].
#
# Do not allocate extra space for another array,
# you must do this by modifying the input array in-place with O(1) extra memory.
#
# You may assume all the characters consist of printable ascii characters.
#
# Example 1:
# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
#
# Example 2:
# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
#


def reverse_string(s: [str]) -> None:  # 투 포인터를 이용한 스왑, 2개의 포인터를 이용해 범위 조정
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


def reverse_string2(s: [str]) -> None:  # 파이썬다운 방식
    s.reverse()
    # s[:] = s[::-1]  # 슬라이싱은 리스트에서도 사용가능, 변수 할당 처리에 오류가 날 수 있어 값을 복사하는 트릭
