import math
def solution(progresses, speeds):
    answer = []
    res = 0
    while len(progresses) > 1 :
        if math.ceil((100-progresses[0]) / speeds[0]) >= math.ceil((100-progresses[1]) / speeds[1]):
            res += 1
            del progresses[0]
            del speeds[0]
        else:
            res += 1
            answer.append(res)
            res = 0
            del progresses[0]
            del speeds[0]
    res += 1
    answer.append(res)
    return answer
   
