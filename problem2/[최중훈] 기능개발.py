import math

def solution(progresses, speeds):
    # 각 프로그램의 개발완료까지 며칠 걸리는지 리스트 생성
    days = [math.ceil((100-p)/s) for p,s in zip(progresses,speeds)] # math 라이브러리를 사용해서 소수점 올림

    finish = 0 # 배포까지 걸리는 일자
    all = [] # 각 프로그램을 얼마만에 배포할 수 있을지를 담을 리스트 생성
    for i in days:
        if i > finish:
            finish = i # 개발이 완료되기까지 기간이 앞 프로그램보다 길다면 새로운 일정 추가
        all.append(finish)
    print(all)

    # 리스트 내에서 중복값을 카운트해서 딕셔너리화
    count = {}
    for a in all:
        try: count[str(a)] += 1 # a가 정수형이기 때문에 문자화 하지 않으면 제대로 담기지 않음
        except: count[str(a)] = 1
    # print(count)

    answer = list(count.values())
    
    return answer
