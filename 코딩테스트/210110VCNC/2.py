import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *


def solution(links):
    groups = []
    reader, answer = 0, 0
    links.reverse()
    # 그룹 구분
    group = []
    for i in range(len(links)):
        if i == len(links) - 1:
            groups.append(group)
        if links[i][0] != reader:
            reader = links[i][0]
            if i != 0:
                groups.append(group)
                group = []
            group.append(reader)
            group.append(links[i][1])
        else:
            group.append(links[i][1])
    print(groups)
    # 그룹당 한명만 참가하는 경우의 수 세기

    # 자연수 10^9 + 7로 나누었을 때의 나머지를 return
    return answer % (10 ** 9 + 7)


print(solution([[4, 5], [4, 3], [4, 2], [1, 6], [7, 4], [7, 1]]))
print(solution([[3, 5], [3, 2], [6, 3], [6, 1], [4, 6]]))
