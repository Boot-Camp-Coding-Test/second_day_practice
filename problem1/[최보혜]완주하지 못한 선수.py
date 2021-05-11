from collections import Counter

def solution(participant, completion):
    participant = Counter(participant) # participant dict형태 count
    completion = Counter(completion) # completion dict형태 count
    answer = participant-completion # 빼서 하나 남기기
    return list(answer.keys())[0] # 그냥 anwer[0]은 values값 나오기 때문에 key를 리스트로 바꿔서 출력
