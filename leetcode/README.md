# leetcode

### 210107

- [x] 125. Valid Palindrome (문자열) [문제](https://leetcode.com/problems/valid-palindrome/) [풀이](https://github.com/jaehui327/algorithm/tree/master/leetcode#125-%EC%9C%A0%ED%9A%A8%ED%95%9C-%ED%8C%B0%EB%A6%B0%EB%93%9C%EB%A1%AC)
- [x] 344. Reverse String(문자열) [문제](https://leetcode.com/problems/reverse-string/) [풀이]


### 210108

- [x] 937. Reorder Data in Log Files(문자열) [문제](https://leetcode.com/problems/reorder-data-in-log-files/) [풀이]
- [x] 819. Most Common Word(문자열) [문제](https://leetcode.com/problems/most-common-word/) [풀이]
- [x] 49. Group Anagrams(문자열) [문제](https://leetcode.com/problems/group-anagrams/) [풀이]
- [x] 5. Longest Palindrome Substring(문자열) [문제](https://leetcode.com/problems/longest-palindromic-substring/) [풀이]


### 210111

- [x] 1. Two Sum(배열) [문제](https://leetcode.com/problems/two-sum/) [풀이](https://github.com/jaehui327/algorithm/tree/master/leetcode#1-%EB%91%90%EC%88%98%EC%9D%98-%ED%95%A9)
- [ ] 42. Trapping Rain Water(배열) [문제](https://leetcode.com/problems/trapping-rain-water/) [풀이]




---
### 파이썬의 기본 라이브러리
```python
import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *
```
---



## 문자열
### 125. 유효한 팰린드롬

leetcode 125. Valid Palindrome

'팰린드롬'이란
앞뒤가 똑같은 단어나 문장, 우리말로는 '회문'이라고 부른다.
ex) 소주 만 병만 주소

*주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.*

```python
def is_palindrome(self, s: str) -> bool:  
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)
    return s == s[::-1]  
```

```
💡 문자열 슬라이싱
매우 편리하고 무엇보다 내부적으로 매우 빠르게 동작한다.
위치를 지정하면 해당 위치의 배열 포인터를 얻게 되며,
이를 통해 연결된 객체를 찾아 실제 값을 찾아낸다.
이 과정은 매우 속도가 빠르므로 문자열 조작 시에는 항상 슬라이싱을 우선적으로 사용하는 편이 속도 개선에 유리하다.
```

```python
>>> S = '안녕하세요'
>>> print(S[1:4)
녕하세
>>> print(S[1:-2])
녕하
>>> print(S[:-3])
안녕
>>> print(S[-3:]
하세요

# 인덱스를 둘 다 생략하면 사본을 리턴한다.
# 파이썬은 a = b 와 같은 형태로 할당하면 
# 변수의 값이 할당되는 것이 아니라 a 변수가 b 변수를 참조하는 형태가 된다.
# 참조가 아닌 값 복사를 위해 [:]를 사용할 수 있으며,
# 이 방식은 문자열이나 리스트를 복사하는 Pythonic Way이기도 하다.
>>> print(S[:])
안녕하세요

# 뒤집기
>>> print(S[::1])
요세하녕안
```



## 배열
### 1. 두수의 합

leetcode 1. Two Sum

*덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.*

```
💡  브루트 포스 (Brute-Force)
모든 조합을 더해서 일일이 확인해보는 무차별 대입 방식
```

- 브루트 포스보다 파이썬의 내부 함수로 구현된 `in` 은 훨씬 더 빨리 실행된다.
- 모든 조합을 비교하지 않고, 타겟에서 첫 번째 값을 뺀 값, `target - num` 이 존재하는지 탐색해보자.
- 비교나 탐색 대신, 한번에 정답을 찾을 수 있는 방법:

    두 번째 수를 키로 하고, 인덱스를 값으로 하여 딕셔너리로 저장

- 전체를 저장할 필요 없이 정답을 찾게되면 함수를 바로 빠져나올 수 있도록 조회 구조를 개선해보자.

```python
def two_sum(nums: [int], target: int) -> [int]:
    nums_map = {}
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i
```