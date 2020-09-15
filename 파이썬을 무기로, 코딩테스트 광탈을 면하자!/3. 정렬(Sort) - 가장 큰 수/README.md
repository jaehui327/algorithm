# 3. 정렬(Sort) 대표 문제 풀이: 가장 큰 수
## solution
```python
def solution(numbers):
    numbers = [str(x) for x in numbers]
    numbers.sort(key=lambda x : (x * 4)[:4], reverse=True)
    if numbers[0] == '0':
        answer = '0'
    else:
        answer = ''.join(numbers)
    return answer
```
