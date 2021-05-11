#코드를 좀 많이 다듬어야될것 같지만 일단 올려두고..
import math

def solution(progresses, speeds):
    result = []
    num = 1
    max_date = math.ceil((100-progresses[0])/speeds[0])

    
    for i in range(len(progresses))[1:] :
        date = math.ceil((100-progresses[i])/speeds[i])

        if max_date < date :
            max_date = date
            result.append(num)
            num = 1
        else :
            num += 1

    result.append(num)
    
    answer = result
    return answer
