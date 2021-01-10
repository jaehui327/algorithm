import collections
import re


def solution(lottos):
    # 당첨 번호와 보너스 번호 구분
    goals, bonuses, answers = [], [], []
    bonus = 0
    answer = ''
    for lotto in lottos:
        goals += [int(goal) for goal in lotto.split(' ') if goal.isdigit()]
        bonuses += [int(bonus[1:-1]) for bonus in re.sub('^[0-9]', ' ', lotto).split() if not bonus.isdigit()]
    goals.sort()
    bonuses.sort()
    # 출현 빈도수
    goals_counts = collections.Counter(goals)
    bonuses_counts = collections.Counter(bonuses)
    bonuses_counts.subtract([1, 2, 3, 4, 5, 6, 7])
    # 오름차순
    for num in goals_counts.most_common(6):
        answers.append(num[0])
    for bon in bonuses_counts.most_common():
        if bon[0] not in answers:
            bonus = bon[0]
            answers.append(bonus)
            break
    answers.sort()
    # 보너스 번호 괄호
    for ans in answers:
        if ans == bonus:
            answer += '%c%d%c ' % ('(', ans, ')')
        else:
            answer += str(ans) + ' '
    return answer.rstrip()


print(solution(["10 18 23 33 (15) 29 45", "42 (5) 45 32 15 23 12", "19 6 12 16 35 34 (17)", "(15) 23 26 21 20 37 12", "15 20 39 9 (18) 5 12", "18 (20) 11 5 22 21 25", "42 44 23 8 5 22 (20)"]))
print(solution(["15 10 39 5 1 21 (22)", "11 5 (10) 39 1 8 44", "(39) 10 5 22 15 9 20", "22 10 5 1 (15) 3 2", "10 (5) 22 1 15 41 38", "10 5 39 33 17 14 (1)"]))
