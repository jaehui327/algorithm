# leetcode

### 210107

- [x] 125. Valid Palindrome (문자열) [문제](https://leetcode.com/problems/valid-palindrome/) [풀이]
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