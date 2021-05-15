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

# =======================================================
# 재도전

def solution(progresses, speeds) :
    answer = []
    
    # 지난 일수 담을 리스트
    days = [0] * len(progresses)
    
    # progresses, speeds, days zip으로 묶기
    # 이 때 zipped 는 [(),(),()] 형태로 나옴
    zipped = list(zip(progresses,speeds,days))
    
    # map 활용해서 [[],[],[]] 형태로 바꾸기
    # 이렇게 해준 이유는 tuple 는 immutable 하므로 list 로 바꿔줌
    new_zipped = list(map(list,zipped))
    count=0
    while True :
        for i in range(len(new_zipped)) :
            
            # 만약 progress 가 100 이상이면 그냥 continue
            if new_zipped[i][0] >= 100 :
                continue
            
            # 그 외 상황에서는 progress 에 speed 만큼 더해주기
            new_zipped[i][0]+=new_zipped[i][1]
            
            # 지난 일수 days 1씩 업데이트 하기
            new_zipped[i][2]+=1
            
            # 100 이상되면 그냥 100으로 간주하고 count 1 증가
            if new_zipped[i][0] >= 100 :
                new_zipped[i][0] = 100
                count+=1
        
        # progress 가 모두 100이 될 때 break 에서 whilte loop 나오기
        if count == len(new_zipped) : 
            break
        
    curr_max = new_zipped[0][2]
    answer.append(0)
    
    # max 값 업데이트 해주기
    for i in range(len(new_zipped)) : 
        if new_zipped[i][2]<= curr_max : 
            answer[-1]+=1
        else :
            curr_max=new_zipped[i][2]
            answer.append(1)

    return answer

# Key Points
    # 처음 풀었을 때에는 이전값과 비교해서 이전값보다 작으면 1씩 증가, 이전값보다 크면 answer list에 1 append 했음
    # 예를 들어 지난 일 수가 [7,2,4,5] 이면 최종적으로 봤을 때 7일 날 4 개의 기능이 모두 배포가 됨 ==> answer = [4] 여야함
    # 이전 방식으로 풀었으면 [2,1,1] 이렇게 출력되서 에러 발생!
    # max 값을 업데이트 하는 방식으로 바꿔서 풀었더니 성공함
