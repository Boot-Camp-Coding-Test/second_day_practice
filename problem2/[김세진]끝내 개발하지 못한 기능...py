def solution(progresses, speeds):
    answer = []
    
    while progresses:
        count = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            
            if progresses[0]>=100:
                progresses.pop(0)
                speeds.pop(0)
                count+=1
            
            else:
                if count>0:
                    answer.append(count)
    return answer
                
    
    ## 틀렸어요.... 안돌아가요... 모르겠어요.... 엄마....

        

        
