def solution(participant, completion):
    for i in completion:
        participant.remove(i)
        
    return participant[0]
