#
# 937. Reorder Data in Log Files
#
# You have an array of logs.  Each log is a space delimited string of words.
#
# For each log, the first word in each log is an alphanumeric identifier.  Then, either:
#
# Each word after the identifier will consist only of lowercase letters, or;
# Each word after the identifier will consist only of digits.
# We will call these two varieties of logs letter-logs and digit-logs.
# It is guaranteed that each log has at least one word after its identifier.
#
# Reorder the logs so that all of the letter-logs come before any digit-log.
# The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.
# The digit-logs should be put in their original order.
#
# Return the final order of the logs.
#
# Example 1:
# Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
#


def reorder_log_files(logs: [str]) -> [str]:  # 람다와 + 연산자 이용
    letters, digits = [], []
    for log in logs:  # 숫자와 문자 구분
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    # 2개의 키를 람다 표현식으로 정렬
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))  # 식별자를 제외한 문자열 [1:]을 키로 하여 정렬, 후순위로 식별자 [0]을 지정
    return letters + digits
