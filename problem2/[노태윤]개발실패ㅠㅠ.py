# 실패작

def solution(progresses, speeds) :
    answer = []
    days = [0] * len(progresses)
    zipped = list(zip(progresses,speeds,days))
    new_zipped = list(map(list,zipped))
    count=0
    while True :
        for i in range(len(new_zipped)) :
            if new_zipped[i][0] >= 100 :
                continue

            new_zipped[i][0]+=new_zipped[i][1]
            new_zipped[i][2]+=1
            if new_zipped[i][0] >= 100 :
                new_zipped[i][0] = 100
                count+=1
                
        if count == len(new_zipped) : 
            break
    
    answer.append(1)
    for j in range(0,len(new_zipped)) :
        if j == 0 :
            continue
        if new_zipped[j][2] <= new_zipped[j-1][2] :
            answer[-1]+=1
        else :
            answer.append(1)

    return answer
