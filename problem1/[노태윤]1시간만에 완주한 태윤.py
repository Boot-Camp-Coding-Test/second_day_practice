from collections import Counter

def solution(participant, completion):
    part_counter = Counter(participant)
    comp_counter = Counter(completion)
    
    answer = list(set(part_counter.items()).difference(set(comp_counter.items())))[0][0]
    return answer
