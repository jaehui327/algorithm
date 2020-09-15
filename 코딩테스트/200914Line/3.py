def solution(n):
    answer = []
    count = 0
    low = 0
    high = 0
    while n > 10:
        mid = int(len(n)) / 2
        for i in range(0, mid):
            low += n % 10
            print("low: ", low)
        high = n >> mid
        n = low + high
        count += 1
    answer = [count, n]
    return answer

res1 = solution(73425)
print("res1: ",res1)