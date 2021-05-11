# 완주하지 못한 선수 https://programmers.co.kr/learn/courses/30/lessons/42576

from collections import Counter

def solution1(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]


def solution2(participant, completion):     
    # 줄세워서 차례로 확인하면서 나아감
    participant.sort()
    completion.sort()
    for i, j in zip(participant, completion):
        if i != j:
            return i
    return participant[-1] # iteration 중간에 확인되지 않으면 젤 뒤에 있는 값을 반환
