import re
def solution(new_id):
    # 1. 대 -> 소
    answer = new_id.lower()
    # print("1. ", answer)
    # 2. 불가 문자 제거
    answer = re.sub('[^0-9a-z-_.]', '', answer)
    # print("2. ", answer)
    # 3. . 연속 -> 하나로 치환
    answer = re.sub('\.+', '.', answer)
    # print("3. ", answer)
    # 4. . 처음. 끝 제거
    if answer[0] == '.':
        answer = answer[1:]
    if len(answer) != 0:
        if answer[len(answer) - 1] == '.':
            answer = answer[:len(answer) - 1]
    # print("4. ", answer)
    # 5. 빈 문자열, a 대입
    if answer == "": answer = "a"
    # print("5. ", answer)
    # 6. 16자 이상, 뒤쪽 제거
    if len(answer) > 15: answer = answer[:15]
    if answer[len(answer) - 1] == '.':
        answer = answer[:len(answer) - 1]
    # print("6. ", answer)
    # 7. 2자 이하, 마지막 문자 길이 3까지 반복
    if len(answer) < 3:
        while len(answer) < 3:
            answer += answer[-1]
    # print("7. ", answer)
    return answer

res1 = solution("...!@BaT#*..y.abcdefghijklm")
print("res1 : ", res1)
res2 = solution("z-+.^.")
print("res2 : ", res2)
res3 = solution("=.=")
print("res3 : ", res3)
res4 = solution("123_.def")
print("res4 : ", res4)
res5 = solution("abcdefghijklmn.p")
print("res5 : ", res5)