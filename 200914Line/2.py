def solution(ball, order):
    answer = []
    for i in range(len(order) - 1, -1, -1):
        for j in range(0, i + 1):
            if order[j] == ball[0]:
                answer.append(ball[0])
                ball.pop(0)
                order.pop(j)
                break
            elif order[j] == ball[-1]:
                answer.append(ball[-1])
                ball.pop(-1)
                order.pop(j)
                break
        # print(answer, ball, order)
    return answer

res1 = solution([1, 2, 3, 4, 5, 6], [6, 2, 5, 1, 4, 3])
print("res1: ", res1)