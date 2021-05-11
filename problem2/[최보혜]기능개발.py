def solution(progresses, speeds):
    
    # 걸리는 날짜를 계산한 Q 리스트 만들기
    Q = []
    for i,j in zip(progresses, speeds):
        x = (100 - i) // j
        if (100-j)%j!=0: # 값이 나누어 떨어지지 않았다면 1 더하기
            x+=1
        Q.append(x) # Q리스트에 추가
    
    # result 구하기
    result, i = [], 0 # result: 결과 담을 리스트, i: 인덱스
    cnt = 1 # count
    check = Q[i] # 기준점이 되는 값 (비교할 값)
    while True:
        if i+1 == len(Q): # 마지막 값이면 cnt 추가하고 while문 종료
            result.append(cnt)
            break
        if check<Q[i+1]: # 기준값보다 값이 크면 cnt추가
            result.append(cnt)
            cnt = 1 # cnt값 원래대로
            check = Q[i+1] # 기준값은 그 다음 인덱스값으로 바꿔주기
        else: # 기준값보다 작으면 cnt 더하기
            cnt+=1
        i+=1 # 인덱스 더하기
    return result

solution([93, 30, 55], 	[1, 30, 5]) # [2, 1]
solution([95, 90, 99, 99, 80, 99], 	[1, 1, 1, 1, 1, 1]) # [1, 3, 2]
solution([98, 99, 97, 96], [1, 1, 1, 1]) # [2,1,1]
solution([40, 93, 30, 55, 60, 65], [60, 1, 30, 5, 10, 7]) #[1,2,3]
solution([93, 30, 55, 60, 40, 65],  [1, 30, 5 , 10, 60, 7]) # [2,4]
