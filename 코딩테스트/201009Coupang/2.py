def solution(n, customers):
    # 도착날짜 도착시간 소요시간
    #  MM/DD  HH:MM:SS MM
    kiosk = {}
    cus = []
    for i in range(len(customers)):
        cus.append(list(map(int, customers[i].replace('/', " ").replace(":", " ").split())))
    print(cus)
    for i in range(len(cus)):
        time = 0
        # 키오스크 갯수만큼 고객 받기
        if i < n:
            time = cus[i][5]
            # 키오스크 운영 완료 시간 = 고객 도착 시간 + 소요 시간
            if cus[i][3] + time >= 60:
                if cus[i][2] == 24:
                    break
        else:
            # 비어있는 키오스크 중 운영되지 않은 시간이 긴 키오스크 찾기
            for j in range(n):
                break
            # 가장 빨리 끝나는 키오스크 찾기
            for j in range(n):
                break
    answer = 0
    return answer

print(solution(3, ["10/01 23:20:25 30", "10/01 23:25:50 26", "10/01 23:31:00 05", "10/01 23:33:17 24", "10/01 23:50:25 13", "10/01 23:55:45 20", "10/01 23:59:39 03", "10/02 00:10:00 10"]))
print(solution(2, ["02/28 23:59:00 03","03/01 00:00:00 02", "03/01 00:05:00 01"]))


