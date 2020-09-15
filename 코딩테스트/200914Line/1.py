def solution(boxes):
    answer = 0
    count = 0
    # 1. 이미 맞는 짝 제거
    for box in boxes:
        if box[0] == box[1]:
            box[0:2] = [0, 0]
    # print("1. ", boxes)
    # 2. 짝 맞추기
    for i in range(0, len(boxes) - 1):
        for _ in range(0, 2):
            for j in range(i + 1, len(boxes)):
                for k in range(0, 2):
                    # print("변경 전: ",boxes[i][k], boxes[j][k])
                    if boxes[i][k] == boxes[j][k]:
                        boxes[i][k] = 0
                        boxes[j][k] = 0
                    if k == 0:
                        if boxes[i][k] == boxes[j][k + 1]:
                            boxes[i][k] = 0
                            boxes[j][k + 1] = 0
                    if k == 1:
                        if boxes[i][k] == boxes[j][k - 1]:
                            boxes[i][k] = 0
                            boxes[j][k - 1] = 0
                    # print("변경 후: ", boxes[i][k], boxes[j][k])
    print("2. ", boxes)
    # 모자란 것 상자개수 만큼 채우기
    for box in boxes:
        if box[0] == 0:
            count += 1
        if box[1] == 0:
            count += 1
        print(box, "count: " , count)
    answer = int(len(boxes) - count / 2)
    return answer

res1 = solution([[1, 2], [2, 1], [3, 3], [4, 5], [5, 6], [7, 8]])
print("res1: ", res1)