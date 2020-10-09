def solution(k, score):
    answer = 0
    sub = []
    count = {}
    an = []
    for i in range(len(score) - 1):
        sub.append(score[i] - score[i + 1])
    # print(sub)
    for s in sub:
        try: count[s] += 1
        except: count[s] = 1
    # print(count)
    for key, val in count.items():
        if key > 1 and val > 1:
            an.append(key)
    # print(an)
    for i in range(len(sub)):
        for a in an:
            if sub[i] == a:
                score[i] = 0
                score[i + 1] = 0
    # print(score)
    for s in score:
        if s != 0:
            answer += 1
    return answer

print(solution(3, [24,22,20,10,5,3,2,1]))
print(solution(2, [1300000000,700000000,668239490,618239490,568239490,568239486,518239486,157658638,157658634,100000000,100]))