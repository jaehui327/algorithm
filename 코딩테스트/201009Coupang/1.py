def solution(N):
    answer = [1, 1]
    mul = [1 for _ in range(10)]
    # print(mul)
    for i in range(2, 10):
        n = N
        # print("i = ", i)
        while 1:
            if n % i == 0:
                n //= i
            elif n > i:
                mul[i] = mul[i] * n % i
                n = (n - n % i) // i
            elif 1 < n < i:
                mul[i] = mul[i] * n
                break
            else:
                break
            # print("n = ", n, ", mul[i] = ", mul[i])
    print(mul)
    for i in range(8):
        if answer[1] <= mul[i + 1]:
            answer[0] = i + 1
            answer[1] = mul[i + 1]
    return answer

print(solution(10))
print(solution(14))