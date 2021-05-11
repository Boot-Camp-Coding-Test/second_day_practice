#case1

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(participant)-1]


#case2

import collections
def solution(participant, completion):
    a = (collections.Counter(participant) - collections.Counter(completion))
    return list(a.keys())[0]
