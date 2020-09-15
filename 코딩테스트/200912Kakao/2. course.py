from itertools import combinations
def solution(orders, course):
    answer = []
    count = {}
    # 1. 문자열의 조합 구하기
    c = []
    for order in orders:
        order = ''.join(sorted(order))
        # print(order1)
        for i in range(len(order)):
            for j in combinations(order, i + 1):
                c.append(''.join(j))
    # print("1. ", c)
    # 2. 조합에서 크기 1인 문자열 삭제
    for i in range(0, len(c)):
        if len(c[i]) < 2:
            c[i] = ''
    c = ' '.join(c).split()
    c.sort(key=len)
    # print("2. ", c)
    # 3. 중복 개수 2 이상
    for i in c:
        try: count[i] += 1
        except: count[i] = 1
    for i in c:
        if count[i] == 1:
            count.pop(i)
    print("3. count: ", count)
    # 4. 스카피의 추가하고 싶어하는 코스요리의 단품 메뉴들의 갯수 반영
    # 리스트 만들어서 return
    for r in count:
        for j in course:
            if count[r] == j:
                answer.append(r)
    answer.sort()
    return answer

res1 = solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])
print("res1 : ", res1)
res2 = solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5])
print("res2 : ", res2)
res3 = solution(["XYZ", "XWY", "WXA"], [2,3,4])
print("res3 : ", res3)