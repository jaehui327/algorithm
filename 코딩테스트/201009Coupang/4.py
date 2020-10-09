def solution(depar, hub, dest, roads):
    answer = 0
    # 출발지 -> 물류센터 경우의 수 + 물류센터 -> 도착지 경우의 수
    depar = route(depar, hub, roads)
    des = 0
    for r in roads:
        des += route(hub, dest, roads)
    answer = depar + des
    return answer

def route(dep, des, roads):
    print(dep, des, roads)
    count = 0
    for r in roads:
        if dep == r[0]:
            if des == r[1]:
                count += 1
            else:
                roads.remove(r)
                route(r[0], des, roads)
        else:
            break
    return count

print(solution("SEOUL", "DAEGU", "YEOSU", [["ULSAN","BUSAN"],["DAEJEON","ULSAN"],["DAEJEON","GWANGJU"],["SEOUL","DAEJEON"],["SEOUL","ULSAN"],["DAEJEON","DAEGU"],["GWANGJU","BUSAN"],["DAEGU","GWANGJU"],["DAEGU","BUSAN"],["ULSAN","DAEGU"],["GWANGJU","YEOSU"],["BUSAN","YEOSU"]]))
print(solution("ULSAN", "SEOUL", "BUSAN", [["SEOUL","DAEJEON"],["ULSAN","BUSAN"],["DAEJEON","ULSAN"],["DAEJEON","GWANGJU"],["SEOUL","ULSAN"],["DAEJEON","BUSAN"],["GWANGJU","BUSAN"]]))
