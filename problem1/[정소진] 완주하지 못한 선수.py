# 1 / 통과
def solution(participant, completion):
    
    participant.sort()
    completion.sort()

    for i in range(len(participant)):
        if participant[i] != completion[i]:
            return participant[i]
          
# 2 / 시간 초과..
def solution(participant, completion):
  
    for i in range(len(participant)):
          if participant[i] not in completion:
              return participant[i]
          
          completion.remove(participant[i])


