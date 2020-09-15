def solution(info, query):
    answer = []
    applier = []
    check = []
    # 1. info 공백 구분 배열 생성
    for i in info:
        applier.append(i.split())
    # print("1. ", applier)
    # 2. query 공백 구분 배열 생성
    for q in query:
        # 2 - 1. and 삭제
        q = q.replace("and", "")
        # 2 - 2. 공백 제거
        check.append(q.split())
    # print("2 .", check)
    # 3. query 순서대로 info와 비교
    for c in check:
        count = 0
        for a in applier:
            able = True
            for i in range(0, 5):
                # print(c, a, count)
                if i == 4:
                    if int(a[i]) >= int(c[i]):
                        continue
                    else:
                        able = False
                        break
                else:
                    if c[i] == '-' or c[i] == a[i]:
                        continue
                    elif c[i] != a[i]:
                        able = False
                        break
            if able:
                count += 1
            # print(c, a, count)
        answer.append(count)
    return answer

res1 = solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])
print("res1 : ", res1)