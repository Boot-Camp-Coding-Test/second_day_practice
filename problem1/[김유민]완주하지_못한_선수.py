def solution(participant, completion):
    participant.sort()
    completion.sort()
    completion.append(' ')

    pair = zip(participant, completion)
    for p in pair :
        if p[0] != p[1] :
            return p[0]
